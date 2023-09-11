def get_digit_name(n):
    """
    -------------------------------------------------------
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    -------------------------------------------------------
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    -------------------------------------------------------
    """
    names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] 
    name = names[n]

    return name

def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """

    # Sort values list ascending order
    values.sort()

    # First index is smallest
    smallest = values[0]
    # Last index is largest
    largest = values[-1]
    total = 0

    # Iterate and sum all values
    for val in values:
        total += val

    # Divide by length for average
    average = total / len(values)

    return (smallest, largest, total, average)

def many_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        indexes - a list of indexes of the location of value in values,
            [] if not found (list of int).
    -------------------------------------------------------
    """

    indexes = []

    # Iterate of an enumerated values list
    for idx, val in enumerate(values):
        # Append index to indexes if equal
        if val == value:
            indexes.append(idx)

    return indexes

def min_search(values):
    """
    -------------------------------------------------------
    Searches through values for the minimum value(s) and returns a
    list of the indexes of those values. (Assumes values has at least
    one element.)
    User: indexes = min_search(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
    Returns:
        indexes - a list of indexes of the minimum values in
            values (list of int).
    -------------------------------------------------------
    """


    indexes = []
    
    # Get minimum value
    min = values[0]
    for val in values:
        if val <= min:
            min = val
    
    # Append all instances of minimum value
    for idx, val in enumerate(values):
        if val == min:
            indexes.append(idx)
        
    return indexes

def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sums(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """

    target = [] 

    # Iterate over a range of the list length
    for idx in range(0, len(source1)):
        # Sum the two lists at the same index
        target.append(source1[idx])
        target[idx] += source2[idx]

    return target

