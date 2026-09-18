#!/usr/bin/env python3
"""Assemble preserved experiment pages and a post-lab PDF into one A4 report."""

from __future__ import annotations

import argparse
import io
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps
from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}


def image_page(path: Path) -> PdfReader:
    image = Image.open(path).convert("RGB")
    image = ImageOps.autocontrast(image, cutoff=0.4)
    image = ImageEnhance.Brightness(image).enhance(1.03)
    image = ImageEnhance.Contrast(image).enhance(1.05)
    image = ImageEnhance.Sharpness(image).enhance(1.07)
    encoded = io.BytesIO()
    image.save(encoded, format="JPEG", quality=94, optimize=True)
    encoded.seek(0)

    page = io.BytesIO()
    page_w, page_h = A4
    margin = 18
    scale = min((page_w - 2 * margin) / image.width, (page_h - 2 * margin) / image.height)
    draw_w, draw_h = image.width * scale, image.height * scale
    pdf = canvas.Canvas(page, pagesize=A4)
    pdf.setFillColorRGB(1, 1, 1)
    pdf.rect(0, 0, page_w, page_h, stroke=0, fill=1)
    pdf.drawImage(ImageReader(encoded), (page_w - draw_w) / 2, (page_h - draw_h) / 2,
                  draw_w, draw_h, preserveAspectRatio=True, mask="auto")
    pdf.showPage()
    pdf.save()
    page.seek(0)
    return PdfReader(page)


def reader_for(path: Path) -> PdfReader:
    if path.suffix.lower() == ".pdf":
        return PdfReader(str(path))
    if path.suffix.lower() in IMAGE_SUFFIXES:
        return image_page(path)
    raise ValueError(f"Unsupported page source: {path}")


def numbered_pages(reader: PdfReader, start: int | None) -> list:
    pages = []
    for index, source_page in enumerate(reader.pages):
        if start is not None:
            width, height = float(source_page.mediabox.width), float(source_page.mediabox.height)
            overlay = io.BytesIO()
            pdf = canvas.Canvas(overlay, pagesize=(width, height))
            pdf.setFont("Helvetica", 9)
            pdf.setFillColorRGB(0.35, 0.38, 0.42)
            pdf.drawCentredString(width / 2, 18, str(start + index))
            pdf.save()
            overlay.seek(0)
            source_page.merge_page(PdfReader(overlay).pages[0])
        pages.append(source_page)
    return pages


def add_sources(writer: PdfWriter, paths: list[Path]) -> int:
    count = 0
    for path in paths:
        for page in reader_for(path).pages:
            writer.add_page(page)
            count += 1
    return count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prelab", nargs="+", type=Path, required=True)
    parser.add_argument("--raw", nargs="+", type=Path, required=True)
    parser.add_argument("--postlab", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--number-postlab-from", type=int)
    parser.add_argument("--title", default="大学物理实验完整实验报告")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    inputs = [*args.prelab, *args.raw, args.postlab]
    missing = [str(path) for path in inputs if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing input: " + ", ".join(missing))

    writer = PdfWriter()
    prelab_count = add_sources(writer, args.prelab)
    raw_start = prelab_count
    raw_count = add_sources(writer, args.raw)
    postlab_start = prelab_count + raw_count
    postlab_reader = PdfReader(str(args.postlab))
    for page in numbered_pages(postlab_reader, args.number_postlab_from):
        writer.add_page(page)

    writer.add_outline_item("实验预习", 0)
    writer.add_outline_item("实验现象与原始数据记录", raw_start)
    writer.add_outline_item("课后报告", postlab_start)
    writer.add_metadata({"/Title": args.title, "/Subject": "大学物理实验"})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("wb") as handle:
        writer.write(handle)

    result = PdfReader(str(args.output))
    expected = prelab_count + raw_count + len(postlab_reader.pages)
    if len(result.pages) != expected:
        raise RuntimeError(f"Page count mismatch: expected {expected}, got {len(result.pages)}")
    print(f"Created {args.output} ({expected} pages)")


if __name__ == "__main__":
    main()
