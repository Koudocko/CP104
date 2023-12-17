"""
-------------------------------------------------------
Exam Task 3 Function Definitions
-------------------------------------------------------
Author: Tyler Wehrle
ID:     169056772
Email:  wehr6772@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""


def upper_vowels(string):
    """
    -------------------------------------------------------
    Converts vowels in a string to upper-case, all other 
    letters to lower-case. Non letters are left unchanged.
    Vowels include: aeiou.
    Use: altered = upper_vowels(string)
    -------------------------------------------------------
    Parameters:
        string - string to process (str)
    Returns‌​‌​​​​‌​​‌‌‌​​‌‌​‌​​​​​​‌​​:
        altered - the resulting string (str)
    -------------------------------------------------------
    """

    # Your code here
    vowels = ['a', 'e', 'i', 'o', 'u']
    altered = ""

    for char in string:
        if vowels.count(char) != 0:
           altered += chr(ord(char) - 32)
        else:
           altered += char

    return altered
