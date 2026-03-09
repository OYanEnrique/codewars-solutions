'''
Quarter of the year:
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

Constraint:

1 <= month <= 12
'''

def quarter_of(month):
    return 1 if month>=1 and month<=3 else 2 if month >=4 and month <=6 else 3 if month >= 7 and month <= 9 else 4 if month >=10 and month <=12 else 'invalid number'