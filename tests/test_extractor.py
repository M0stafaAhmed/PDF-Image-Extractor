import base64
import tempfile
import unittest
from pathlib import Path

import pymupdf

from pdf_image_extractor import extract_images_from_pdf


PNG_BYTES = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jZioAAAAASUVORK5CYII="
)


class ExtractImagesTests(unittest.TestCase):
    def test_extracts_an_embedded_image(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            pdf_path = root / "fixture.pdf"
            output_dir = root / "images"

            document = pymupdf.open()
            page = document.new_page()
            page.insert_image(page.rect, stream=PNG_BYTES)
            document.save(pdf_path)
            document.close()

            count = extract_images_from_pdf(str(pdf_path), str(output_dir))

            self.assertEqual(count, 1)
            extracted = list(output_dir.glob("image_1_1.*"))
            self.assertEqual(len(extracted), 1)
            self.assertGreater(extracted[0].stat().st_size, 0)

    def test_empty_pdf_returns_zero(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            pdf_path = root / "empty.pdf"
            document = pymupdf.open()
            document.new_page()
            document.save(pdf_path)
            document.close()

            count = extract_images_from_pdf(
                str(pdf_path),
                str(root / "empty_images"),
            )

            self.assertEqual(count, 0)


if __name__ == "__main__":
    unittest.main()
