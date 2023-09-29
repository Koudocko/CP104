"""
-------------------------------------------------------
Deterins if a list of strings has a word chain.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import has_word_chain

# Set words list
words = ['camel', 'leopard', 'dog', 'giraffe', 'elephant']

# Get if word chain exists
word_chain = has_word_chain(words)

# Display if word chain exists
print(f"word_chain({words}) -> {word_chain}")
