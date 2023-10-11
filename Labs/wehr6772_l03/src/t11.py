"""
-------------------------------------------------------
Aligns strings in various horizontal formats
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

# Location strings
location1 = "left"
location2 = "middle"
location3 = "right"

# Format/align the location strings
print(f"{location1:-<20s}") # Left align
print(f"{location2:-^20s}") # Middle align
print(f"{location3:->20s}") # Right align
