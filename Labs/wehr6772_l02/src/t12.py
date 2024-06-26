"""
-------------------------------------------------------
Converts total seconds into larger time units
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Constants
# Number of seconds in a minute
SECONDS_IN_MINUTE = 60 
# Number of seconds in an hour
SECONDS_IN_HOUR = SECONDS_IN_MINUTE * 60
# Number of seconds in a day
SECONDS_IN_DAY = SECONDS_IN_HOUR * 24

# Obtain total seconds
num_total_seconds = int(input("Number of seconds: "))
# Get number of days
num_days = num_total_seconds // SECONDS_IN_DAY
num_total_seconds %= SECONDS_IN_DAY # Set remainder
# Get number of hours
num_hours = num_total_seconds // SECONDS_IN_HOUR
num_total_seconds %= SECONDS_IN_HOUR # Set remainder
# Get number of minutes
num_minutes = num_total_seconds // SECONDS_IN_MINUTE
# Get number of seconds remaining
num_seconds = num_total_seconds % SECONDS_IN_MINUTE

# Display number of days, hours, minutes, and seconds from total seconds
print(f"Days: {num_days} Hours: {num_hours} Minutes: {num_minutes} Seconds: {num_seconds}")
