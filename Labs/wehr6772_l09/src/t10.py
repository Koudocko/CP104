"""
-------------------------------------------------------
Counts the number of attributes in the text
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import text_analyze

# Get input text
txt = input("Enter some text: ")

# Get text attributes
uppr, lowr, dgts, whtspc = text_analyze(txt)

# Display attirbutes of text
print(f"text_analyze({txt}) -> ({uppr}, {lowr}, {dgts}, {whtspc})")
