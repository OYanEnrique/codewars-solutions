'''
Divide and Conquer:
Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.

Return as a number.
'''
def div_con(x):
    str_num = sum([int(num) for num in x if isinstance(num, str)])
    int_num = sum([int(num) for num in x if isinstance(num, int)])
    return int_num - str_num