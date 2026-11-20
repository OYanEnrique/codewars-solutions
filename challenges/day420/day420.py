'''

Training JS #32: methods of Math---round() ceil() and floor():

From this lesson, we learn about some math functions in Python. Some are built-in (no import needed), however others are imported from the math module. This module has many helpful functions, however we will only be focusing on a few.

See here for more information about the math module

math module
In this lesson we learn three methods to turn a number into an integer: round(), math.ceil() and math.floor().

Their definitions and detailed information:

round()
math.ceil()
math.floor()
First of all, we have to understand the first thing, all three of these are regular functions, not methods. It means that you need to use them like this: math.round(1.23). Not like this: (1.23).round().

Here we use some examples to understand their usage:

print(round(1.45))      # output:1
print(math.ceil(1.45))  # output:2
print(math.floor(1.45)) # output:1
print(round(1.55))      # output:2
print(math.ceil(1.55))  # output:2
print(math.floor(1.55)) # output:1
We can see, ceil() always rounding up to get a large integer; floor() always rounding down to get a small integer; round() according to the fractional part and round it to integer.

When the parameter is negative, they still works:

print(round(-1.45))      # output:-1
print(math.ceil(-1.45))  # output:-1
print(math.floor(-1.45)) # output:-2
print(round(-1.55))      # output:-2
print(math.ceil(-1.55))  # output:-1
print(math.floor(-1.55)) # output:-2
Ok, lesson is over. let's us do some task.

Task
Coding in function roundIt. function accept 1 parameter n. It's a number with a decimal point. Please use different methods based on the location of the decimal point, turn the number into an integer.

If the decimal point is on the left side of the number (that is, the count of digits on the left of the decimal point is less than that on the right), Using ceil() method.

roundIt(3.45) should return 4
If the decimal point is on the right side of the number (that is, the count of digits on the left of the decimal point is more than that on the right), Using floor() method.

roundIt(34.5) should return 34
If the decimal point is on the middle of the number (that is, the count of digits on the left of the decimal point is equals that on the right), Using round() method.

roundIt(34.56) should return 35
'''
from math import ceil, floor

def round_it(n):
    str_n = str(n).split('.')
    return ceil(n) if len(str_n[0]) < len(str_n[1]) else floor(n) if len(str_n[0]) > len(str_n[1]) else round(n)
