'''
Simple validation of a username with regex:
Write a simple regex to validate a username. Allowed characters are:

lowercase letters,
numbers,
underscore
Length should be between 4 and 16 characters (both included).
'''
def validate_usr(username):
    import re
    return re.fullmatch(r'^[a-z0-9_]{4,16}$', username) is not None