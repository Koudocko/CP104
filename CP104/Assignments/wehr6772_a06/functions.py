def total_wins():
    """
    -------------------------------------------------------
    Queries the winning teams and returns the final score
    of both purple and gold teams.
    Use: total_wins()
    -------------------------------------------------------
    Returns:
        purple_count - number of times purple won (int)
        gold_count - number of times gold won (int)
    ------------------------------------------------------
    """

    # Initialize counter variables
    purple_count = 0
    gold_count = 0

    while True:
        winning_team = input("Enter the winning team: ")

        # If something is input
        if winning_team != "":
            # Increment purple wins if purple
            if winning_team == "purple":
                purple_count += 1
            # Increment gold wins if gold
            elif winning_team == "gold":
                gold_count += 1
        # Break if empty input
        else:
            break

    return (purple_count, gold_count)

def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """

    prime = True
    factor = 2

    while factor < number:
        if number % factor == 0:
            prime = False
            break

        factor += 1

    return prime

def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """


    print(f"Principal: ${principal_amount:9.2f}") 
    print(f"Interest interest_rate : {interest_rate:.2f}%") 
    print(f"Monthly payment: ${payment:.2f}%") 


    print(f"{'':-^34s}")
    print(f"Month Interest   Payment   Balance")
    print(f"{'':-^34s}")

    # Turn annual interest rate into a decimal montly interest rate
    monthly_interest_rate = interest_rate / 12 / 100
    # Initialze month counter at 1
    month = 1

    while principal_amount > 0:
        # Compute interest amount gained
        interest = principal_amount * monthly_interest_rate

        # Prevent balance from going into negative
        if principal_amount < payment - interest:
            payment = principal_amount + interest
            principal_amount = 0
        # Deduct payment, add interest
        else:
            principal_amount -= payment - interest
        

        print(f"{month:>5d}{interest:>9.2f}{payment:>10.2f}{principal_amount:>10.2f}")
        month += 1 

    return

import time
def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """

    # Initialize digits counter
    digits = 0

    # Loop until no more digits are left
    while number != 0:
        # If negative, convert to positive, remove digit, convert back
        if number < 0:
            number = -((-number) // 10)
        # If positive, remove digit
        else:
            number //= 10

        # Incrememnt digits counter
        digits += 1

    return digits

def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """

    # Initialze total and current factor being tested
    total = 0
    factor = 1

    # Loop until the potential factor is the same as the number
    while factor < number:
        # If evenly divisible, add factor total
        if number % factor == 0:
            total += factor

        factor += 1

    return total
