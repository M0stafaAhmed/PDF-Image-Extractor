"""PDF image extractor desktop application.

Extracts embedded raster images from each page of a PDF into a sibling folder.
"""

from __future__ import annotations

import os
import tkinter as tk
from tkinter import filedialog, messagebox

try:
    import pymupdf
except ImportError:
    pymupdf = None


def extract_images_from_pdf(pdf_path: str, output_folder: str) -> int:
    """Extract embedded images from a PDF and return the number written."""
    if pymupdf is None:
        raise RuntimeError(
            "PyMuPDF is not installed. Install the project dependencies with "
            "'python -m pip install -r requirements.txt'."
        )

    os.makedirs(output_folder, exist_ok=True)
    image_count = 0

    with pymupdf.open(pdf_path) as pdf_file:
        for page_index in range(len(pdf_file)):
            page = pdf_file[page_index]
            images = page.get_images(full=True)

            for img_index, image_info in enumerate(images):
                xref = image_info[0]
                extracted = pdf_file.extract_image(xref)
                image_bytes = extracted["image"]
                image_ext = extracted["ext"]

                image_filename = os.path.join(
                    output_folder,
                    f"image_{page_index + 1}_{img_index + 1}.{image_ext}",
                )
                with open(image_filename, "wb") as image_file:
                    image_file.write(image_bytes)

                image_count += 1

    return image_count


def select_pdf(root: tk.Tk) -> None:
    """Prompt for a PDF and run the extraction."""
    file_path = filedialog.askopenfilename(
        parent=root,
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf")],
    )
    if not file_path:
        return

    pdf_name = os.path.splitext(os.path.basename(file_path))[0]
    output_folder = os.path.join(
        os.path.dirname(file_path),
        pdf_name + "_images",
    )

    try:
        count = extract_images_from_pdf(file_path, output_folder)
        messagebox.showinfo(
            "Extraction complete",
            f"Extracted {count} images.\nSaved in:\n{output_folder}",
            parent=root,
        )
    except Exception as exc:
        messagebox.showerror("Extraction failed", str(exc), parent=root)


def main() -> int:
    """Create and run the Tkinter application."""
    root = tk.Tk()
    root.title("PDF Image Extractor")
    root.geometry("400x200")

    label = tk.Label(
        root,
        text="Extract embedded images from a PDF",
        font=("Arial", 12),
    )
    label.pack(pady=20)

    button = tk.Button(
        root,
        text="Select PDF and Extract",
        command=lambda: select_pdf(root),
        font=("Arial", 11),
    )
    button.pack(pady=20)

    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
