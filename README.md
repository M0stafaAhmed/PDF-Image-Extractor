# PDF Image Extractor

A small Tkinter desktop utility that extracts embedded image objects from a selected PDF and saves them into a sibling folder.

## What it does

1. Opens a file picker for a PDF.
2. Reads each page and enumerates embedded image objects.
3. Extracts the original image bytes through PyMuPDF.
4. Writes files named `image_<page>_<index>.<extension>`.
5. Creates an output folder next to the source PDF, named `<pdf-name>_images`.

This extracts embedded image objects. It does not take screenshots of pages or reconstruct images that exist only as vector drawings.

## Repository layout

| Path | Purpose |
|---|---|
| `pdf_image_extractor.py` | Canonical application entry point and extraction function |
| `PDFImageExtractor.spec` | PyInstaller build definition for the canonical entry point |
| `p_d_f_image_extractor.py` | Earlier alternative implementation retained for reference; not used by the build spec |
| `requirements.txt` | Runtime dependency |
| `requirements-build.txt` | Windows packaging dependency |
| `tests/test_extractor.py` | Regression tests for embedded-image extraction and empty PDFs |

## Development setup (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run the application:

```powershell
python .\pdf_image_extractor.py
```

Run the regression tests:

```powershell
python -m unittest discover -s tests -v
```

## Build a Windows executable

Install build requirements:

```powershell
pip install -r requirements-build.txt
```

Build from the repository root:

```powershell
pyinstaller --clean --noconfirm .\PDFImageExtractor.spec
```

The executable is written to `dist\\PDFImageExtractor.exe`. The spec bundles the application and its dependencies into one executable.

## Dependency and licensing note

The application depends on PyMuPDF. PyMuPDF is offered under the GNU AGPL or a commercial license from Artifex. Before redistributing this application, choose a distribution model that complies with the PyMuPDF license terms. The repository does not currently grant a separate license for the application source.

See the [PyMuPDF license information](https://pymupdf.readthedocs.io/en/latest/about.html).

## Status

The canonical script and spec are aligned. The regression tests have been added but have not yet been executed in a clean Windows build environment. Keep this repository private until the tests and packaged executable have been verified.