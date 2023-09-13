def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """

    # Initialze new empty string
    spaced = '' 

    # Iterate over chaarcters in sentence
    for idx, character in enumerate(sentence):
        # If character is upper case, add a space
        if character.isupper():
            spaced += ' '
        
        # If first letter in sentence, keep uppercase
        if idx == 0:
            spaced += character
        # Concatenate current character (remove uppercase)
        else:
            spaced += character.lower()

    # Strip front and end whitespace to cleanup
    spaced = spaced.strip()

    return spaced

def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """

    # If ends with "s", "sh", or "ch" add "es"
    if (
        string.endswith("s") or
        string.endswith("sh") or
        string.endswith("ch")
        ): 
        pluralized = string + "es"
    # If ends with "y" and not "ay" or "oy" remove "y" and add "ies"
    elif (
        string.endswith("y") and
        not (
            string.endswith("ay") or
            string.endswith("oy"))
        ):
        pluralized = string[0:-1] + "ies"
    # Anything else, add "s"
    else:
        pluralized = string + "s"

    return pluralized

def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """

    # Index offset starting at end
    index = -1
    # Initalize suffix to empty (default)
    suffix = ""

    # While the slice from the index to the end 
    # of str1 is the same as the end of str2
    # and does not pass the start of str1
    while (
            str2.endswith(str1[index:len(str1)]) and
            index >= -len(str1)
        ):
        # Safe to set suffix to end slice
        suffix = str1[index:len(str1)]
        # Move index closer to front
        index -= 1 
        
    return suffix

def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """

    # Set default to true
    is_valid = True

    # Set last digit to blank initially
    last_digit = ""
    # Iterate over all digits
    for digit in isbn:
        # If it's neither a digit or hyphen, break
        if not digit.isdigit() and digit != '-':
            is_valid = False
            break
        # If 5 groups of digits exist
        elif (digit == '-' and last_digit == '-' or isbn.count('-') != 4):
            is_valid = False
            break

        # Update last digit
        last_digit = digit

    # Get first 3 digits
    first_group = isbn[0:3]
    # Check that first 3 digits is 978 or 979
    if first_group != "978" and first_group != "979":
        is_valid = False

    # Check that ISBN length is 17
    if len(isbn) != 17:
        is_valid = False


    return is_valid

def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """

    # Word chain is true unless proven otherwise
    word_chain = True
    # First word edge case, must be equal
    prev_word = words[0][0]

    # Iterate over the words
    idx = 0
    while idx < len(words):
        # If first letter of current does not equal last letter of previous
        if words[idx][0] != prev_word[-1]:
            word_chain = False

        # Set previous word to current
        prev_word = words[idx]
        # Increment iterator count
        idx += 1
    
    return word_chain
