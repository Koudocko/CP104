"""
-------------------------------------------------------
Computes the difference between two input digits
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Get two digits
digits = int(input("Enter a positive digit number: "))

# Compute first digit in 10s column
first_digit = digits // 10
# Computes second digit in 1s column
second_digit = digits % 10
# Compute difference between the two
difference = first_digit - second_digit

# Display the difference between the digits
print(f"The difference of the digits of {digits} is {difference}")
