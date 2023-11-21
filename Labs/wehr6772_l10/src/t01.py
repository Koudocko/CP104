"""
-------------------------------------------------------
Read nth customer record in customers.txt file
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import customer_record

print("Find record n")

# Get record number
n = int(input("Enter a record number: "))

# File handle
fh = open("customers.txt", "r")

# Get and display nth customer record
result = customer_record(fh, n)
print(result)

fh.close()
