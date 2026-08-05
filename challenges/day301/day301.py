'''
Product Of Maximums Of Array (Array Series #2):
Task
Given an array/list [] of integers , Find the product of the k maximal numbers.

Notes
Array/list size is at least 3 .

Array/list's numbers Will be mixture of positives , negatives and zeros

Repetition of numbers in the array/list could occur.

Input >> Output Examples
maxProduct ({4, 3, 5}, 2) ==>  return (20)
'''
from math import prod
def max_product(lst, n_largest_elements):
    return prod([n for n in sorted(lst, reverse=True)[:n_largest_elements]])