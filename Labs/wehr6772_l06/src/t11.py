"""
-------------------------------------------------------
Calculates the total a worker earns before retirement
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import retirement

# Get worker's information 
age = int(input("Input worker's age: "))
salary = float(input("Input worker's salary: "))
increase = float(input("Input worker's increase: "))

# Display table of worker's salary until they retire
print(f"retirement({age}, {salary}, {increase}) ->")
retirement(age, salary, increase)
