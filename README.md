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

The expected one-file output is `dist\PDFImageExtractor.exe`. The optional `PDFImageExtractor.ico` is used when present; the application works without it.

## Dependency and licensing note

The application depends on PyMuPDF. PyMuPDF is offered under the GNU AGPL or a commercial license from Artifex. Before redistributing this application, choose a distribution model that complies with the PyMuPDF license terms. The repository does not currently grant a separate license for the application source.

See the [PyMuPDF license information](https://pymupdf.readthedocs.io/en/latest/about.html).

## Status

The canonical script and spec are aligned. The Windows workflow runs regression tests and builds the executable. Keep the repository private until the distribution license and ownership questions are settled.

## License and permissions

See [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md) for important dependency-specific licensing information.

This repository is **proprietary; all rights reserved**. You may view it where access is granted. For a public repository, GitHub's Terms of Service permit users to view and fork it on GitHub. Those platform permissions do not grant a general right to reuse, modify, redistribute, sublicense, or commercially exploit the original material outside GitHub.

Obtain prior, express, written permission from the copyright holder before any such use beyond the rights GitHub grants. Sending a request is not approval; wait for written authorization. See [LICENSE](./LICENSE) for the full scope, exclusions, permission-request route, and treatment of earlier license grants.

**Third-party material:** This notice covers only original material that the repository owner owns or is authorized to license. Third-party software, images, fonts, trademarks, curricula, standards, datasets, contributions, and other external content remain subject to their respective rights and terms. This repository does not relicense them.

**Dependency licensing:** This application depends on PyMuPDF, which is offered under the GNU AGPL or a commercial license. The proprietary notice here applies only to original application material; it does not relicense PyMuPDF or remove its obligations. Review the AGPL terms or obtain the appropriate commercial license before distributing a proprietary application. See [PyMuPDF licensing](https://pymupdf.io/licensing) and [the documentation](https://pymupdf.readthedocs.io/en/latest/about.html).
