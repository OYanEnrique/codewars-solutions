'''
Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!
'''

def capitalize(s):
        newst = ''
        x=''
        for index,alpha in enumerate(s):
            if index %2 == 0:
                newst = newst + alpha.lower()
                x=x+alpha.upper()
            else:
                newst = newst + alpha.upper()
                x=x + alpha.lower()
        return [x, newst]