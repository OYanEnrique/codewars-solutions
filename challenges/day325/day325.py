'''
Fuel Calculator: Total Cost:
In this kata you will have to write a function that takes litres and price_per_litre (in dollar) as arguments.

Purchases of 2 or more litres get a discount of 5 cents per litre, purchases of 4 or more litres get a discount of 10 cents per litre, and so on every two litres, up to a maximum discount of 25 cents per litre. But total discount per litre cannot be more than 25 cents. Return the total cost rounded to 2 decimal places. Also you can guess that there will not be negative or non-numeric inputs.

Good Luck!

Note
1 Dollar = 100 Cents
'''
def fuel_price(litres, price_per_litre):
    discount = 0.25 if litres >= 10 else 0.20 if litres >= 8 else 0.15 if litres >= 6 else 0.10 if litres >= 4 else 0.05
    return round((price_per_litre * litres) - (discount * litres), 2)