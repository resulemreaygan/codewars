"""
Author: Resul Emre AYGAN
"""

"""
Project Description: Square Every Digit

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""


def square_digits(num):
    # return int(''.join(map(str, list(map(lambda x: pow(x, 2), map(int, str(num)))))))
    return int(''.join(str(pow(int(item), 2)) for item in str(num)))
