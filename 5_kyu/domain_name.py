import re

"""
Author: Resul Emre AYGAN
"""

"""
Project Description: Extract the domain name from a URL

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

Note: This question is not well prepared. The test is insufficient. 
Therefore, the answer produced is insufficient and specific to this kata.
"""


def domain_name(url):
    return re.search(r'(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
