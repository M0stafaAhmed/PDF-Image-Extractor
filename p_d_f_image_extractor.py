import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Try to import the correct 'fitz' from PyMuPDF.
# If the wrong 'fitz' package is installed (the one that requires 'frontend'),
# or PyMuPDF isn't installed, we'll set fitz = None and handle it gracefully.
try:
    import fitz  # PyMuPDF
    # Heuristic: PyMuPDF exposes 'open'; the unrelated 'fitz' often lacks it or is broken.
    if not hasattr(fitz, "open"):
        raise ImportError("Wrong 'fitz' module detected")
except Exception:
    fitz = None


def extract_images_from_pdf(pdf_path, output_folder):
    if fitz is None:
        raise RuntimeError(
            "PyMuPDF (package name 'pymupdf') is not available or a conflicting 'fitz' package is installed.\n\n"
            "Fix:\n"
            "  pip uninstall -y fitz\n"
            "  pip install -U pymupdf"
        )
    # Use context manager to ensure the PDF is closed properly
    with fitz.open(pdf_path) as pdf_file:
        image_count = 0
        for page_index in range(len(pdf_file)):
            page = pdf_file[page_index]
            images = page.get_images(full=True)

            for img_index, img in enumerate(images):
                xref = img[0]
                base_image = pdf_file.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]

                image_count += 1
                image_filename = os.path.join(
                    output_folder, f"image_{page_index + 1}_{img_index + 1}.{image_ext}"
                )
                with open(image_filename, "wb") as img_file:
                    img_file.write(image_bytes)

        return image_count


def select_pdf():
    file_path = filedialog.askopenfilename(
        title="Select PDF File", filetypes=[("PDF Files", "*.pdf")]
    )
    if not file_path:
        return

    # Create output folder with same name as PDF
    pdf_name = os.path.splitext(os.path.basename(file_path))[0]
    output_folder = os.path.join(os.path.dirname(file_path), pdf_name + "_images")
    os.makedirs(output_folder, exist_ok=True)

    try:
        count = extract_images_from_pdf(file_path, output_folder)
        messagebox.showinfo("Done", f"Extracted {count} images.\nSaved in:\n{output_folder}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI Setup
root = tk.Tk()
root.title("PDF Image Extractor")
root.geometry("400x200")

label = tk.Label(root, text="Extract original images from a PDF", font=("Arial", 12))
label.pack(pady=20)

button = tk.Button(root, text="Select PDF and Extract", command=select_pdf, font=("Arial", 11))
button.pack(pady=20)

root.mainloop()
