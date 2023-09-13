"""
-------------------------------------------------------
Generates a multiplication table based on range.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import multiplication_table

# Get start and stop numbers
start_num = int(input("Start number: "))
stop_num = int(input("Stop number: "))

# Display multiplication table
print(f"multiplication_table({start_num}, {stop_num}) ->")
multiplication_table(start_num, stop_num)
