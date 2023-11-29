"""
-------------------------------------------------------
Displays statistics about the student's grades in students.txt.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import student_stats

# Open file handle to students.txt as read
file_handle = open("students.txt", "r", encoding="utf-8")

# Get the students.txt statistics
l_id, h_id, avg = student_stats(file_handle)

# Display students stats
print(f"student_stats(file_handle) -> {l_id}, {h_id}, {avg}")

# Close file handle
file_handle.close()
