'''
Simple string characters:
In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters (everything else), as follows.
The order is: uppercase letters, lowercase letters, numbers and special characters.
"*'&ABCDabcde12345" --> [ 4, 5, 5, 3 ]
'''
import re
def solve(s):
    special = re.findall(r"[^a-zA-Z0-9\s]", s)
    lowercase = re.findall(r"[a-z]", s)
    uppercase = re.findall(r"[A-Z]", s)
    numbers = re.findall(r"[0-9]", s)
    return [len(uppercase), len(lowercase), len(numbers), len(special)]