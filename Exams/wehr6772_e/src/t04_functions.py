"""
-------------------------------------------------------
Exam Task 4 Function Definitions
-------------------------------------------------------
Author: Tyler Wehrle
ID:     169056772
Email:  wehr6772@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""


def draw_x(height):
    """
    -------------------------------------------------------
    Prints a X shape height characters high.
    Use: draw_x(height)
    -------------------------------------------------------
    Parameters:
        height - maximum height in characters of X shape (int >= 3)
    Returns‌​‌​​​​‌​​‌‌‌​​‌‌​‌​​​​​​‌​​:
        None
    -------------------------------------------------------
    """

    # Your code here
    for curr in range(0, height):
        if curr < (height // 2):
            lpad = curr
        else:
            lpad = height - curr - 1
        rpad = height - (2 * lpad) - 2;

        if rpad < 0:
            print(f"{'':{lpad}s}#")
        else:
            print(f"{'':{lpad}s}#{'':{rpad}s}#")

    return
