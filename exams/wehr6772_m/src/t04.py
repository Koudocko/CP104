"""
-------------------------------------------------------
Midterm A Task 4 Testing
-------------------------------------------------------
Author: Tyler Wehrle
ID:     169056772
Email:  wehr6772@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Imports
# your imports here
from t04_functions import result

# your code here

response = input("Enter response: ")

classification = result(response)

print(f"result({response}) -> {classification}")
