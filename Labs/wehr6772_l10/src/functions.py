"""
-------------------------------------------------------
Lab 10 functions
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty ist otherwise (list)
    -------------------------------------------------------
    """

    # Initialize result list
    result = fh.readline()

    # Read until result is reached or end of file
    while result != "" and n > 0:
        result = fh.readline()
        n -= 1

    # Test for out of bounds record
    if result == "":
        result = []
    else:
        result = result.strip().split(',')

    return result 


def number_stats(fh):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """

    # Get first number
    line = fh.readline()
    number = int(line)

    # Set initial values
    numbers_len = 1
    smallest = number
    largest = number
    total = number

    # Run until end of file
    while line != "":
        # Get every subsequent number
        line = fh.readline()

        # Safe guard at end of file
        if line != "":
            number = int(line)

            # Update largest and smallest accordingly
            if number < smallest:
                smallest = number
            elif number > largest:
                largest = number

            # Update total and amount processes
            total += number
            numbers_len += 1

    # Compute average of nums
    average = total / numbers_len
    return (smallest, largest, total, average)

def count_frequency_word(fh, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in fh.
    Case is significant - line in file must match word in case.
    Use: count = count_frequency_word(fh, word)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        word - the word to search for it in fh (str)
    Returns:
        count - the number of appearance of word in fh (int)
    ------------------------------------------------------
    """
    
    # Inital word match count
    count = 0

    # Get initial read line
    line = fh.readline().strip()

    while line != "":
        # Process line
        if line == word:
            count += 1

        # Strip leading/following whitespace
        line = fh.readline().strip()

    return count


def find_longest(fh):
    """
    -------------------------------------------------------
    Finds the last word with longest length in fh.
    Assumes file is not empty.
    Use: word = find_longest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the last word with the longest length in fh (str)
    ------------------------------------------------------
    """
    
    # Initialze word variable
    word = ""
    line = " "
    
    # Loop until end of file
    while line != "":
        # Get line from file
        line = fh.readline()
        line = line.strip()

        # Update longest word if current is greater than or equal in length
        if len(line) >= len(word):
            word = line

    return word

def file_copy(fh_1, fh_2):
    """
    -------------------------------------------------------
    Copies the contents of fh_1 to fh_2.
    Any contents of fh_2 are overwritten.
    Use: file_copy(fh_1, fh_2)
    -------------------------------------------------------
    Parameters:
        fh_1 - source file (file handle - already open for reading)
        fh_2 - target file (file handle - already open for writing)
    Returns:
        None
    ------------------------------------------------------
    """

    line = " "

    # Loop until end of file
    while line != "":
        line = fh_1.readline()

        # Copy line to new_words.txt
        fh_2.write(line)

    return
