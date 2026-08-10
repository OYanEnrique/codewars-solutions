'''
The 'if' function:
Create a function that takes three arguments:

a value to be evaluated for truthiness.
a function to execute if the first argument is truthy.
a function to execute if the first argument is falsy.
If the first argument evaluates to truthy, call the second argument (a function). If it evaluates to falsy, call the third argument instead (also a function).
'''
from collections.abc import Callable

def _if(bool, func1: Callable, func2: Callable):
    return func1() if bool else func2()