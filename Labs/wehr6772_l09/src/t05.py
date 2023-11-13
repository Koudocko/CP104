"""
-------------------------------------------------------
Verifies password is strong enough
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import password_strength

# Get password
password = input("Enter password: ")

# Validate where password is strong enough
password_strength(password)
