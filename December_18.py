import time

def fvt(va): #find the index of the first value > 10.
    i = 0
    for c in va:
        if c >= 10:
            return i
        i+= 1
    return -1

def res(st): # read string.
    lo, va, de = [],[],[] # location, value, depth.
    loca = '' # precursor of location
    for c in st:
        if c == '[':
            loca += '0'
        if c == ']':
            loca = loca[:-1]
        if c == ',':
            loca = loca[:-1]+'1'
        if c.isdigit():
           lo.append(loca)
           va.append(int(c))
           de.append(len(loca))
#        print(c,loin,loca, lo, va)
    return lo, va, de

def addlo(sn0, sn1):  # ho, ha, he):
    lo, va, de = sn0
    ho, ha, he = sn1
    return ['0'+st for st in lo]+['1'+st for st in ho], va+ha, [d+1 for d in de] + [d+1 for d in he]

def tre(sn0): # treat the number until it settles.
    lo, va, de = sn0
    while 1:
        while 5 in de:
            i = de.index(5)
            if i > 0:
                va[i-1] += va[i]
            if i < len(de)-2:
                va[i+2] += va[i+1]
            lo,va,de = lo[:i]+[lo[i][:-1]]+lo[i+2:], va[:i]+[0]+va[i+2:], de[:i]+[de[i]-1]+de[i+2:]
        i = fvt(va)
        if i > -1:
            lo,va,de = lo[:i]+[lo[i]+'0',lo[i]+'1']+lo[i+1:], va[:i]+[va[i]//2, va[i]-va[i]//2]+va[i+1:], de[:i]+[de[i]+1, de[i]+1]+de[i+1:]
        else:
            return lo,va,de

def magl(sn0):
    lo, va, de = sn0
    for i in range(len(lo)):
        for j in range(len(lo[i])):
            c = lo[i][j]
            if c == '0' and lo[i][:j]+'1' in [x[:j+1] for x in lo]:
                va[i] *= 3            
            if c == '1':
                va[i] *= 2
    return sum(va)        

start = time.time()
with open('day18v1.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]
#for u in te[1:]:

vas = res(te[0])
for u in te[1:]:
    vas = tre(addlo(vas,res(u)))
print("p1",magl(vas))
print("p2",max([magl(addlo(res(v),res(u))) for u in te for v in te if u != v]), time.time()-start)
