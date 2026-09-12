'''
Age Range Compatibility Equation:

Everybody knows the classic "half your age plus seven" dating rule that a lot of people follow (including myself). It's the 'recommended' age range in which to date someone.

Min = (age / 2) + 7
Max = (age - 7) * 2
Minimum wage <= Your age <= Maximum age
Task
Given an integer (1 <= n <= 100) representing a person's age, return their minimum and maximum age range.

This equation doesn't work when the age <= 14, so if the age <= 14, use this equation instead:

min = age - 0.10 * age
max = age + 0.10 * age
You should floor all your answers so that an integer is given instead of a float (which doesn't represent age). Return your answer in the form "[min]-[max]"

Examples:
age = 27   =>   "20-40"
age = 5    =>   "4-5"
age = 17   =>   "15-20"
'''
def dating_range(age):
    from math import floor
    return f"{floor(age/2) + 7}-{2*(age-7)}" if age > 14 else f"{floor(age - (0.10*age))}-{floor(age + (0.10*age))}"