'''
Encrypt this!:

Description:

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter must be converted to its ASCII code.
The second letter must be switched with the last letter
Keepin' it simple: There are no special characters in the input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
'''
def encrypt_this(text):
    text = text.split()
    final_str = []
    for t in text:
        if len(t) == 1:
            final_str.append(str(ord(t[0])))
        elif len(t) == 2:
            final_str.append(str(ord(t[0])) + t[1])
        elif len(t) >=3:
            final_str.append(str(ord(t[0])) + t[-1] + t[2:-1] + t[1])
    return ' '.join(final_str)