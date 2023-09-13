"""
-------------------------------------------------------
Get the final score of two teams, gold and purple
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import total_wins

# Display total wins from the teams
print(f"total_wins() ->")
purple_count, gold_count = total_wins()
print(f"({purple_count}, {gold_count})")
