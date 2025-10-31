"""
pdf_organizer.py — Sort PDFs into folders by metadata.
"""
from pathlib import Path
import PyPDF2, shutil, logging


def organize_pdfs(src_folder: Path, dst_folder: Path):
dst_folder.mkdir(exist_ok=True)
for pdf in src_folder.glob("*.pdf"):
try:
with open(pdf, "rb") as f:
info = PyPDF2.PdfReader(f).metadata
author = (info.author or "Unknown").replace("/", "_")
target_dir = dst_folder / author
target_dir.mkdir(exist_ok=True)
shutil.copy2(pdf, target_dir / pdf.name)
logging.info(f"Moved {pdf.name} -> {author}/")
except Exception as e:
logging.error(f"Failed {pdf.name}: {e}")
