'''
Insert dashes:

Write a function that takes an integer num (num >= 0) and inserts dashes ('-') between each two odd digits in num.

Examples
454793 ---> "4547-9-3"
     0 ---> "0"
     1 ---> "1"
13579  ---> "1-3-5-7-9"
 86420 ---> "86420"
'''

def insert_dash(num):
    num = str(num)
    dash = ''
    for i, n in enumerate(num):
        if i + 1 < len(num):
            dash += n
            if int(num[i]) % 2 != 0 and int(num[i+1]) % 2 != 0:
                dash += "-"
            else:
                dash += ''
        else:
            dash += n
    return dash