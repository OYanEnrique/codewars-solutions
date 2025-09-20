'''
Given a random non-negative number, 
you have to return the digits of this number within an array in reverse order.
'''

def digitize(n):
    n = str(n)
    list = []
    for numbers in n:
        list.append(int(numbers))
    return list[::-1]