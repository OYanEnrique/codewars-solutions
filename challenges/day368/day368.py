'''
Rot13:

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13.

If there are nonletter characters in the string, they should be left as-is in the output. Only letters from the ASCII alphabet should be shifted, like in the original Rot13 "implementation".
'''
def rot13(message):
    low = 'abcdefghijklmnopqrstuvwxyz'
    upp = low.upper()
    return ''.join([low[(low.index(char)+13)%26] if char.islower() else upp[(upp.index(char)+13)%26] if char.isupper() else char for char in message])
