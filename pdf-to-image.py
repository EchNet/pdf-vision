import sys
import os
from pdf2image import convert_from_path
from PIL import Image
"""
  Convert PDF to image.  Requires poppler.
"""


def pdf_to_merged_image(pdf_path):
  if not pdf_path.lower().endswith(".pdf"):
    print("Error: Input file must be a PDF.")
    return

  images = convert_from_path(pdf_path, dpi=300)

  if not images:
    print("Error: No images extracted from PDF.")
    return

  # Get total width (max width of all pages) and total height (sum of heights)
  total_width = max(img.width for img in images)
  total_height = sum(img.height for img in images)

  # Create blank image
  merged_image = Image.new("RGB", (total_width, total_height))

  # Paste each image one below the other
  y_offset = 0
  for img in images:
    merged_image.paste(img, (0, y_offset))
    y_offset += img.height

  # Save the merged image
  output_path = os.path.splitext(pdf_path)[0] + ".png"  # Replace .pdf with .png
  merged_image.save(output_path, "PNG")
  print(f"Saved merged image as: {output_path}")


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: python pdf-to-image.py input.pdf")
  else:
    pdf_to_merged_image(sys.argv[1])
