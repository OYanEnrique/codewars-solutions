'''
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 '''
def square_sum(numbers):
	save = []
	for number in numbers:
		save.append(number**2)
	return(sum(save))
test = [1,2,2]
print(square_sum(test))