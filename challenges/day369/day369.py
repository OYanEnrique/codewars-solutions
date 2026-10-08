'''
The Deaf Rats of Hamelin

Story:
The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.

But some of the rats are deaf and are going the wrong way!

Task:
How many deaf rats are there?

Legend:
P = The Pied Piper
O~ = Rat going left
~O = Rat going right
Example
ex1 ~O~O~O~O P has 0 deaf rats

ex2 P O~ O~ ~O O~ has 1 deaf rat

ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats
'''
def count_deaf_rats(town):
    town = town.replace(" ", "")
    i = town.index("P")
    left = town[: i]
    right = town[i+1:]
    count = 0
    if left:
        left = [left[i:i+2] for i in range(0, len(left), 2)]
        count += left.count("O~")
    if right:
        right = [right[i:i+2] for i in range(0, len(right), 2)]
        count += right.count("~O")
    return count 