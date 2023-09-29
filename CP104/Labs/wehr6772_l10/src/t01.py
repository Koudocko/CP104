"""
-------------------------------------------------------
Read nth customer record in customers.txt file
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

from functions import customer_record

# Call implemented customer_record function
result = customer_record(open("customers.txt", "r"), 3)
