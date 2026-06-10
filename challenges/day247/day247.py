'''
Highest Scoring Word:
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''
def high(char):
    char_list = char.split()
    word_final = ''
    y = 0
    for i, chr in enumerate(char_list):
        word = str(char_list[i])
        x = sum(ord(c) - 96 for c in word)
        if x > y:
            y = x
            word_final = char_list[i]
    return word_final