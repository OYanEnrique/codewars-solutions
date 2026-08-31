'''
Longest vowel chain:
Description:
The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel substring. Vowels are any of aeiou.

Good luck!
'''
def solve(st):
    import re
    return max([len(v) for v in re.findall(r'[aeiou]{2,}', st, re.IGNORECASE)], default = 1) if st else 0