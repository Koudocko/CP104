"""
-------------------------------------------------------
Validates a given product code's segments
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

from functions import validate_code

# Call implemented validate_code function
category, digits, qualifiers = validate_code('BFG9000x7')
