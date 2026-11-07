# Third-Party Notices

This file identifies important third-party licensing considerations for PDF Image Extractor. It is not a complete software bill of materials (SBOM); inspect the dependency manifests and packaged build contents for the complete component inventory.

## PyMuPDF / MuPDF

PDF Image Extractor uses PyMuPDF, declared in `requirements.txt`.

PyMuPDF and MuPDF are offered under:
- GNU Affero General Public License version 3 (AGPLv3); or
- a commercial license from Artifex.

The proprietary notice in this repository applies only to original application material owned by the repository author. It does not relicense PyMuPDF or MuPDF and does not remove their license obligations.

Before distributing a proprietary build, assess whether the AGPL terms apply to the intended use and distribution model, or obtain an appropriate commercial license from Artifex. Do not assume that adding this repository's proprietary notice makes a combined application proprietary.

Official licensing references:
- https://pymupdf.io/licensing
- https://pymupdf.readthedocs.io/en/latest/about.html

## Build and other dependencies

Build tools and any additional packages listed in `requirements.txt` and `requirements-build.txt` remain subject to their own licenses. Their presence in the build environment does not transfer ownership to this repository author.

## Scope

This notice is informational and does not replace upstream license texts, legal notices, attribution requirements, or commercial agreements. Check the exact versions and modules included in any release.
