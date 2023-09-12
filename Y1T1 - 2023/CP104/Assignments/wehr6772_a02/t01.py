"""
-------------------------------------------------------
Display the project tax report based on total sales
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Constants
ANNUAL_TAX_D = 0.185
ANNUAL_TAX_P = ANNUAL_TAX_D * 100

# Get total sales input
total_sales = int(input("Enter the total sales: $"))
# Calculate tax based on annual tax rate
tax = total_sales * ANNUAL_TAX_D

# Display the tax report
print("Projected Tax Report")
print(f"{'':-^26s}")
print(f"Total sales:   ${total_sales:10,.2f}")
print(f"Annual tax:    %{ANNUAL_TAX_P:10.2f}")
print(f"{'':-^26s}")
print(f"Tax:           ${tax:10,.2f}")
