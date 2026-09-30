'''
Sort by Last Char:

Given a string of words (x), you need to return an array of the words, sorted alphabetically by the final character in each.

If two words have the same last letter, the returned array should show them in the order they appeared in the given string.

All inputs will be valid.
'''
def last(string):
    return sorted(string.split(), key=lambda s: s[-1])