import sys
import os
from pypdf import PdfReader, PdfWriter

if len(sys.argv) != 2:
  print("Usage: python pdf-split.py <input.pdf>")
  sys.exit(1)

input_path = sys.argv[1]
base_name = os.path.splitext(os.path.basename(input_path))[0]

reader = PdfReader(input_path)

for i, page in enumerate(reader.pages):
  writer = PdfWriter()
  writer.add_page(page)

  output_filename = f"{base_name}_{i+1:03d}.pdf"
  with open(output_filename, "wb") as output_file:
    writer.write(output_file)

print("Done splitting PDF.")
