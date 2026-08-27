'''
Row Weights:
Several people are standing in a row divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

Task
Given an array of positive integers (the weights of the people), return a new array / tuple of two integers (depending on your language), whereby the first one is the total weight of team 1, and the second one is the total weight of team 2. Note that the array will never be empty.

Examples
[13, 27, 49] returns [62, 27] or (62, 27).
'''
def row_weights(array):
    return (sum([n for n in array[::2]]), sum([n for n in array[1::2]]))