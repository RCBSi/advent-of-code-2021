import ast 
import time

def stn(st):# string to nested list of lists.
    if isinstance(st,str):
        return ast.literal_eval(st)
    return st

def nts(nl): # nested lists to string.
    if isinstance(nl, list):
        return str(nl)
    return nl
    
def nf(sn): # If any pair is nested inside four pairs, then returrn a pointer to the pair.
    nested_level = 0
    nested_address = [0]*50
    nested_address_pointer = -1
    found_explodable = 0
    new_i = 0
    frnl, frnr, return_package = [],[],[]
    for i in range(len(sn)):
        if sn[i] == '[':
            nested_level += 1
            nested_address_pointer += 1
        if sn[i] == ']':
            nested_level -= 1
            nested_address[nested_address_pointer] = 0
            nested_address_pointer -= 1
        if sn[i] == ',':
            nested_address[nested_address_pointer] += 1
        if sn[i].isdigit() and found_explodable == 0:
            frnl = [i,[x for x in nested_address[:nested_level]]] # first regular number to the left.
        if sn[i].isdigit() and found_explodable == 1 and i > new_i: 
            frnr = [i,[x for x in nested_address[:nested_level]]] # first regular number to the right.
            return return_package, frnl, frnr
        if nested_level == 5 and found_explodable == 0:
            new_i = next_end_bracket(sn,i)
            return_package = (i, new_i, [x for x in nested_address[:4]])
            found_explodable = 1
    if len(return_package) > 0 and len(frnl) > 0:
        return return_package, frnl, None
    elif len(return_package) > 0:
        return return_package, None, None
    else:
        return None

def next_end_bracket(sn,i):
    for j in range(i,len(sn)): 
        if sn[j] == ']':
            return j+1

def pe(sn, ad, v): #snailfish number address "plus equals" value.
    sn = stn(sn)
    if len(ad) == 0:
        return sn + v
    else: 
        sn[ad[0]] = pe(sn[ad[0]], ad[1:], v)
        return sn
    
def rep(sn, ad, v): #snailfish replace address ad with v.
    if len(ad) == 0:
        return v
    else: 
        sn[ad[0]] = rep(sn[ad[0]], ad[1:], v)
        return sn

def rea(sn, ad): #snailfish read sn at address ad.
    sn = stn(sn)
    if isinstance(ad, list):
        if len(ad) == 0:
            return sn
        else: 
            return rea(sn[ad[0]], ad[1:])

def ex(sn): 
    a = nf(nts(sn))
    if a: #  then there is a pair to explode.
        ((b,c,d),e,f) = a
        if e:
            sn = pe(sn, e[1], rea(sn, d)[0])
        if f:
            sn = pe(sn, f[1], rea(sn, d)[1]) 
        return rep(sn, d, 0) # The entire pair is replaced with 0.

def nsp(sn): # needs split.
    sn = nts(sn)
    for i in range(len(sn)-1):
        if sn[i].isdigit() and sn[i+1].isdigit():
            return True
    return False

def sp(sn):
    sn = nts(sn)
    for i in range(len(sn)-1):
        if sn[i].isdigit() and sn[i+1].isdigit():
            for j in range(i,len(sn)):
                if sn[j].isdigit() == 0:
                    n = int(sn[i:j])
                    sn = sn[:i]+str([n//2, n-n//2])+sn[j:]
                    return sn  
    return sn

def needs_treatment(sn):
    if nf(str(sn)):
        return True
    if nsp(sn):
        return True
    return None

def treat(sn):
    if needs_treatment(sn):
        if nf(str(sn)):
            return treat(ex(stn(sn)))
        if nsp(str(sn)):
            return treat(sp(nts(sn)))
    else:
        return sn

def add(sn, sn1):
    x = [stn(sn)]+[stn(sn1)]
    return treat(x)

def ads(tex): # add a sequence of numbers,
    on = stn(tex[0])
    for i in range(1,len(tex)):
        on = add(on,stn(tex[i]))
    return on

def mag(sn):
    sn = stn(sn)
    if isinstance(sn, int):
        return sn
    if isinstance(sn, list):
        return 3*mag(sn[0]) + 2*mag(sn[1])

start = time.time()
with open('day18v1.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]

print("p1",mag(stn(ads(te))))

maxa = 0
te.reverse()
mid = time.time()
for i in range(len(te)):
    for y in te:
        if te[i] != y:
            nm = mag(add(te[i],y))
            if nm > maxa:
                maxa = nm
    if i > 0 and i%7 == 0:
        print("Part of part2", i, maxa, "estimated time", (time.time()-mid)*(100-i)/i)
                
print("Part2:", maxa, "total time", time.time() - start)

# 30 seconds to perform 100^2 additions.
