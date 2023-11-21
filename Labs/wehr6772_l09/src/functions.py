"""
-------------------------------------------------------
Lab 9 functions
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """

    # Slice the string into sub strings
    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:]

    return (pc, pi, pq)

def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise
        digits - True if four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
    -------------------------------------------------------
    """

    # Slice the string into sub strings
    pc, pi, pq = parse_code(product_code)

    # Defaults
    category = False
    digits = False
    qualifiers = False

    # Validate product category
    if len(pc) == 3 and pc == pc.upper() and pc.isalpha():
        category = True 
    # Validate product digits
    if len(pi) == 4 and pi.isdigit():
        digits = True
    # Validate product qualifiers
    if len(pq) > 0 and pq[0].isupper():
        qualifiers = True

    return (category, digits, qualifiers)

def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """

    # Validate password length
    if len(password) < 8:
        print("not long enough")

    # Validate existence of digit(s)
    has_digit = False
    for val in password:
        if val.isdigit():
            has_digit = True
            break

    if not has_digit:
        print("no digits")

    # Validate existence of upper case
    if password == password.lower():
        print("no upper case")

    # Validate existence of lower case
    if password == password.upper():
        print("no lower case")

    return

def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """

    # Initialize return values
    uppr, lowr, dgts, whitspc = 0, 0, 0, 0
    
    # Iterate over txt characters and increment corresponding counter
    for val in txt:
        if val.isupper():
            uppr += 1
        elif val.islower():
            lowr += 1
        elif val.isdigit():
            dgts += 1
        elif val.isspace():
            whitspc += 1

    return (uppr, lowr, dgts, whitspc)

def comma_period_replace(string):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with all commas replaced by a period (str)
    ------------------------------------------------------
    """

    # Replace all commas with periods using built in string method
    out = string.replace(',', '.')

    return out
