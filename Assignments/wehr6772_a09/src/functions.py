"""
-------------------------------------------------------
Assignment 9 functions
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """

    line = " "

    # Loop until counter depletes
    while count > 0 and line != "":
        # Read line
        line = file_handle.readline()

        # Strips whitepspace for test cases
        print(line.strip())
        count -= 1

    return

def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """

    # Initializes empty numbers list
    numbers_list = [] 
    line = " "

    while line != "":
        line = file_handle.readline()

        if line != "":
            # Split entries by comma
            numbers = line.split(',')

            # Iterate over numbers and append int casted numbers to list
            for number in numbers:
                number = number.strip()

                # Only accept numbers
                if number.isdigit():
                    numbers_list.append(int(number))

    return numbers_list

def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """

    # 0 initialize counters
    ucount, lcount, dcount, wcount, rcount = 0, 0, 0, 0, 0
    line = " "

    while line != "":
        line = file_handle.readline()

        # Match cases to increment for each type of character
        for character in line:
            if character.isupper():
                ucount += 1
            elif character.islower():
                lcount += 1
            elif character.isdigit():
                dcount += 1
            elif character.isspace():
                wcount += 1
            else:
                rcount += 1

    return (ucount, lcount, dcount, wcount, rcount)


def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """

    # Initialize counter with 0
    count = 0
    line = " "

    while line != "":
        line = fh_read.readline()

        if line != "":
            # Push line number to beginning of line
            line = f"[{count}] " + line

            # Overwrite line in file
            fh_write.write(line)

        count += 1

    return

def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """

    # 0 initialize sum of grades and entry counter
    grade_sum = 0
    num_entries = 0

    # Default initialize low and high ids
    l_id = "" 
    h_id = "" 

    # Set upper and lower bounds beyond range
    high = -1 
    low = 101 

    # Line default
    line = " "

    while line != "":
        line = file_handle.readline()

        if line != "":
            # Split entry by commas
            student_entry = line.split(',')

            # Parse grade as int
            grade = int(student_entry[3])
            # Store id
            id = student_entry[2]

            # Update high grade if found higher
            if grade > high:
                high = grade
                h_id = id
            # Update low grade if found lower
            if grade < low:
                low = grade
                l_id = id

            # Add grade to sum
            grade_sum += grade
            # Increment number of entries
            num_entries += 1

    # Compute average grade
    avg = grade_sum / num_entries

    return (l_id, h_id, avg)
