def list_factors(number):
    """
    -------------------------------------------------------
    Obtains a list of all the factors of some number.
    Use: factors = list_factors(number)
    -------------------------------------------------------
    Parameters:
        number - number to be tested for factor (int > 0)
    Returns:
        factors - list of factors of number (list of int)
    ------------------------------------------------------
    """

    # Initialize factors with empty list
    factors = []
    
    # Include [1, number)
    for num in range(1, number):
        # If evenly divisible by num, push factor to factors
        if number % num == 0:
            factors.append(num)

    return factors

def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """

    # Initialize number list with empty list
    number_list = []

    # Input loop
    while True:
        number = int(input("Enter a positive number: "))

        # If number is positive, add to back of list
        if number > 0:
            number_list.append(number)
        # If number is zero, break from loop
        elif number == 0:
            break

    return number_list

def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """

    # Initialize index list with empty list
    index_list = []

    # Iterate over numbers with key and val
    for idx, num in enumerate(numbers):
        # If value matches the target, push the key (index)
        if num == target_number:
            index_list.append(idx);

    return index_list

def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """

    # Traverse the list backwards to pop safely
    for idx in range(len(minuend) - 1, -1, -1):
        # Iterate over all subtrahend targets
        for num in subtrahend:
            # Check if current minuend target matche current subtraend target
            if num == minuend[idx]:
                # Pop index and return to out loop if yes
                minuend.pop(idx)
                break

    return 

def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """

    # Set defaults
    in_order = True
    index = -1

    # Set last number to first element
    last = numbers[0]

    # Iterate over numbers list
    for idx, num in enumerate(numbers):
        # If last number is greater than current number
        if num < last:
            # Set state to not in order, break out of loop
            in_order = False
            index = idx
            break
        
        # Update last number
        last = num

    return (in_order, index)
