"""
-------------------------------------------------------
Testing for Task 7: line_lengths
-------------------------------------------------------
Author: Tyler Wehrle
ID:     169056772
Email:  wehr6772@mylaurier.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""
# Imports

# your imports here
from t07_functions import line_lengths

# Your code here
f_in = open("source.txt", "r", encoding="utf-8")
f_short = open("short.txt", "w", encoding="utf-8")
f_long = open("long.txt", "w", encoding="utf-8")

short_lines, long_lines = line_lengths(f_in, f_short, f_long, 16)
f_in.close()
f_short.close()
f_long.close()

print(f"line_lengths(f_in, f_short, f_long, 16)-> ({short_lines}, {long_lines})")
