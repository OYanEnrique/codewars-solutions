'''
Sort Out The Men From Boys:
Now that the competition gets tough it will Sort out the men from the boys .

Men are the Even numbers and Boys are the odd.

Notes
-Return an array/list where Even numbers come first then odds
-Since , Men are stronger than Boys , Then Even numbers in ascending order While odds in descending .
-Array/list size is at least 4 .
-Array/list numbers could be a mixture of positives , negatives .
-Have no fear , It is guaranteed that no Zeroes will exists .
-Repetition of numbers in the array/list could occur , So (duplications are not included when separating).

Input >> Output Examples:
menFromBoys ({7, 3 , 14 , 17}) ==> return ({14, 17, 7, 3}) 
'''
def men_from_boys(arr):
    arr=set(arr)
    arr1 = [n for n in arr if n % 2 == 0]
    arr2= [n for n in arr if n not in arr1]
    return sorted(arr1) + sorted(arr2, reverse=True)