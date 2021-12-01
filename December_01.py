# advent-of-code-2021

import math 

def up(x,y): # boollean "is this an increase"
    if y > x: 
        return 1
    else:
        return 0

with open('day01v1.txt', 'r') as file:
    t = [int(x.strip()) for x in file.readlines()]

mary = [up(t[i],t[i+1]) for i in range(len(t)-1)]
mary2 = [up(t[i],t[i+3]) for i in range(len(t)-3)]

print(sum(mary))
print(sum(mary2))

