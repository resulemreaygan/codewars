import re

"""
Author: Resul Emre AYGAN
"""

"""
Project Description: Split Strings

Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters
then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""


def split_strings(s):
    return re.findall(".{2}", s + "_")
