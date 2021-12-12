# spaghetti again

with open('day10v1.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]

def rp(u): # remove pairs
    for i in range(len(u)):
        for d in ['()','<>','{}','[]']:
            u = u.replace(d,'')
    return u
  
def fm(u): # find first match fail.
    for c in u:
        if c in [')','>','}',']']:
            return c
            u = u.replace(w,'')
            return u 

sc = {')':3,'>':25137,'}':1197,']':57, None:0}

s = [sc[fm(rp(u))] for u in t]
print("Part1:", sum(s))

def cs(st): #completion string sccore
    sl = list(st)
    sl.reverse()
    sco = 0
    for c in sl:
        sco*=5
        sco+={'(': 1 , '[': 2 ,'{': 3 ,'<': 4 }[c]
    return sco

b = [a for a in [rp(u) for u in t] if fm(a) is None]
ct = [cs(a) for a in b]

import numpy
print("Part2:", int(numpy.median(ct)))
