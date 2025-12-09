'''
Description:
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
'''
def solution(s):
    import re
    return re.sub(r'([A-Z])', r' \1', s).strip()
