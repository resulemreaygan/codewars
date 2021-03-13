"""
Author: Resul Emre AYGAN
"""

"""
Project Description: Find The Parity Outlier

You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except
for a single integer N.
Write a method that takes the array as an argument and returns this "outlier" N.
"""


def find_outlier(integers):
    event_count = 0
    odd_count = 0

    for num in integers:
        if num % 2 == 0:
            event_count += 1
            even_temp = num
        else:
            odd_count += 1
            odd_temp = num

        if event_count > 1 and odd_count == 1:
            return odd_temp

        if odd_count > 1 and event_count == 1:
            return even_temp
