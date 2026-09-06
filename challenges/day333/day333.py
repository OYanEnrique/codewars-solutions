'''
Changing letters:

When provided with a String, capitalize all vowels

For example:

Input : "Hello World!"

Output : "HEllO WOrld!"

Note: Y is not a vowel in this kata.
'''
def swap(st):
    return "".join([s.upper() if s.lower() in "aeiou" else s for s in st])