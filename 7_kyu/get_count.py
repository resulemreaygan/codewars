"""
Author: Resul Emre AYGAN
"""

"""
Project Description: Vowel Count

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


def get_count(input_str):
    return sum(map(input_str.count, ['a', 'e', 'i', 'o', 'u']))
