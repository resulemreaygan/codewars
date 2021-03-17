"""
Author: Resul Emre AYGAN
"""

"""
Project Description: Fake Binary

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. 
Return the resulting string.
"""


def fake_bin(x):
    return ''.join(['0' if int(digit) < 5 else '1' for digit in x])
