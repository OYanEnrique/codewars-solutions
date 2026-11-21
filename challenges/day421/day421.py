'''
Move 10:

Move every letter in the provided string forward 10 letters through the alphabet.

If it goes past 'z', start again at 'a'.

Input will be a string with length > 0.
'''
def move_ten(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return ''.join([alphabet[(alphabet.index(char)+ 10) % 26] for char in st])