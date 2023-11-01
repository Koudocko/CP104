"""
-------------------------------------------------------
Midterm A Task 1 Function Definitions
-------------------------------------------------------
Author: Tyler Wehrle
ID:     169056772
Email:  wehr6772@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Constants

# your constants here
TWENTY_VAL = 20
TEN_VAL = 10
FIVE_VAL = 5
LOONIE_VAL = 1


def minimal_change(dollars):
    """
    -------------------------------------------------------
    Breaks down dollars into a minimal number of bills and coins.
    The change can be:
        twenties - bills worth 20 dollars
        tens - bills worth 10 dollars
        fives - bills worth 5 dollars
        loonies - coins worth 1 dollar
    Use: twenties, tens, fives, loonies = minimal_change(dollars)
    -------------------------------------------------------
    Parameters:
        dollars - number of dollars (int >= 0)
    Returns‌​‌​​​​‌​​‌‌‌​​‌‌​‌​​​​​​‌​​:
        twenties - number of $20 bills (int)
        tens - number of $10 bills (int)
        fives - number of $5 bills (int)
        loonies - number of $1 coins (int)
    -------------------------------------------------------
    """

    # your code here
    twenties = dollars // TWENTY_VAL
    dollars = dollars % TWENTY_VAL
    tens = dollars // TEN_VAL
    dollars = dollars % TEN_VAL
    fives = dollars // FIVE_VAL
    dollars = dollars % FIVE_VAL
    loonies = dollars // LOONIE_VAL

    return (twenties, tens, fives, loonies)
