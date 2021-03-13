"""
Author: Resul Emre AYGAN
"""

"""
Project Description: Isograms

An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
"""


def is_isogram(string):
    lower_string = string.lower()
    return True if lower_string and len(set(lower_string)) == len(lower_string) or len(lower_string) == 0 else False
