import os
import sys

# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print(sys.path)

import pymupdf
import pandas as pd
import config
import pymupdf4llm
import pathlib


""""
Extracts data from a pdf file and returns a dataframe
"""


# The following code is used to extract the text from the pdf file

pdf_path = "src/data/documents/Loft space Savings July2024.pdf"

doc = pymupdf.open(pdf_path)
out = open("output.txt", "wb")
for page in doc:
    text = page.get_text().encode("utf-8")
    out.write(text)
    out.write(bytes((12,)))
out.close()

# To change the pdf from a pdf to a markdown file
