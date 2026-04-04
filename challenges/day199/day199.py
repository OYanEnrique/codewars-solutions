'''
Regexp Basics - is it a digit?:
Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a single digit (0-9), false otherwise.
'''
#v1
def is_digit(n):
    return abs(int(n.strip().isdigit())) if len(n)==1 else False

#v2
import re
def is_digit(n):
    return bool(re.fullmatch(r"[0-9]", n))