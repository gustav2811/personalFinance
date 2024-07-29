import os
import sys

# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print(sys.path)

import pymupdf
import pandas as pd
import config


"""
The pdf extraction class
"""
