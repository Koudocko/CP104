"""
-------------------------------------------------------
Midterm A Task 3 Function Definitions
-------------------------------------------------------
Author: Tyler Wehrle
ID:     169056772
Email:  wehr6772@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Constants

# your constants here
BASE_COST = 95.00
EXTRA_COST = 35.00
VIP_DISCOUNT = 0.15

def servicing():
    """
    -------------------------------------------------------
    Determines the cost of getting a car cleaned. The cost is made up of:
        base cost: $95.00
        cost per extra service: $35.00
        VIP discount 15% only if:
            more than 1 extra service purchased
            and purchaser is a VIP
    The function must ask the user for these inputs.
    Use: cost = servicing()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌​​‌‌​‌​​​​​​‌​​:
        cost - cost of cleaning a car based upon the base cost,
            the number of extra services purchased, and VIP discount
            if applicable (float)
    -------------------------------------------------------
    """

    # your code here
    extra_services = int(input("How many extra services are you purchasing? "))
    cost = BASE_COST + (EXTRA_COST * extra_services)

    if extra_services > 1:
        is_vip = input("Are you a VIP member (Y/N)? ")

        if is_vip == "Y":
            cost = cost - (cost * VIP_DISCOUNT)
    else:
        is_vip = "N"

    return cost
