'''
Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence:
Description:
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
"Hi!" --> "H!!"
"!Hi! Hi!" --> "!H!! H!!"
"aeiou" --> "!!!!!"
"ABCDE" --> "!BCD!"
'''

def replace_exclamation(st):
    return ''.join('!' if ch in 'aeiouAEIOU' else ch for ch in st)