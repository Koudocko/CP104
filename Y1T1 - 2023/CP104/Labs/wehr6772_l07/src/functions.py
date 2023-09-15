# Imports
from random import randint

def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """

    # Generate random target number
    number = randint(1, high)
    # Enter first guess
    guess = int(input("Guess: "))
    count = 1

    # Keep asking for another guess if wrong and increment the counter 
    while guess != number:
        if guess < number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

        guess = int(input("Guess: "))
        count += 1

    # Congratulations once loop exits
    print("Congratulations - good guess!")
    print(f"You made {count} guesses.")

    return count

def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """

    
    exponent = 0
    # Keep incrementing exponent until power of two is >= to target
    while 2 ** exponent < target:
        exponent += 1

    # Evaluate exponent with base 2
    power = 2 ** exponent
    return power

def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """

    final = 1
    base = 1
    # Keep incrementing exponent until power of two is >= to target
    while final < target:
        base += 1
        final += base ** 2

    return final

def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """

    # Get first expense
    expense = float(input("Enter an expense (0 to quite): $"))

    # Set first changes
    balance = available
    expenses = expense 
    balance -= expense

    while expense != 0:
        # Get subsequent expenses
        expense = float(input("Enter another expense (0 to quite): $"))

        # Set subsequent changes
        expenses += expense
        balance -= expense


    # Determine status based on loop exit state of balance
    if balance > 0:
        status = "Surplus"
    elif balance < 0:
        status= "Deficit"
    else:
        status = "Balanced"

    return (expenses, balance, status)

def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """

    # Constants
    TAX_RATE_P = 3.625
    TAX_RATE_D = 1 - (TAX_RATE_P / 100)
    OVERTIME_RATE = 1.5
    OVERTIME = 40

    # Initialie 0 defaults
    employee_count = 0
    total = 0

    # Get initial employee id
    employee_id = int(input("Employee ID: "))

    # Loop while employee id is not 0
    while employee_id != 0:
        # Get employee hourly wage and hours worked
        hourly_wage_rate =  int(input("Hourly wage rate: "))
        hours_worked =  int(input("Hours worked: "))

        # Initialize netpayment for employee
        net_payment = 0
        # Increment number of employees logged
        employee_count += 1

        # Special behaviour for overtime hours
        if hours_worked > OVERTIME:
            # Add overtime paid hours to net payment
            net_payment = (hours_worked - OVERTIME) * hourly_wage_rate * OVERTIME_RATE
            # Reset to remaining normal hours
            hours_worked = OVERTIME

        # Compute net payment for regular hours
        net_payment += hourly_wage_rate * hours_worked
        # Add tax rate on top at the end
        net_payment *= TAX_RATE_D
        
        # Add employee net payment to the total
        total += net_payment

        # Display net payment for the employee
        print(f"Net payment for employee {employee_id}: ${net_payment:,.2f}\n")

        # Get next employee id
        employee_id = int(input("Employee ID: "))

    # Compute average from total and number of employees
    average = total / employee_count

    return (total, average)
        
