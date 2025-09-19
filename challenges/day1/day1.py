'''Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.'''

def sum_array(numbers):
	return 0 if len(numbers) == 0 else sum(numbers)
	
array = [1,2,-2,2.5]
a2 = [-1,-2,-3]
a3 = []
print(sum_array(a3))