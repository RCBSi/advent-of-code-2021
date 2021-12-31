import time
start = time.time()

def mt(x,dx): #move-to
    if (x+dx)%10 == 0:
        return 10
    return (x+dx)%10

def play1(x,y,xs,ys,cl):
    x = mt(x,(cl+1)*3)
    xs += x
    if xs >= 1000:
        return x,y,xs,ys,cl+3
    y = mt(y,(cl+4)*3)
    ys += y
    return x,y,xs,ys,cl+6

def pl(x,y,xs,ys,cl):
    while xs < 1000 and ys < 1000:
        x,y,xs,ys,cl = play1(x,y,xs,ys,cl)
    return min(xs,ys)*(cl-1)

with open('day21v0.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]

print("p1",pl(7,10,0,0,1)) # test: pl(4,8,0,0,1)

ct = [0 for i in range(10)]
for d1 in range(1,4): 
    for d2 in range(1,4): 
        for d3 in range(1,4):
            ct[(d1+d2+d3)%10]+= 1
ct = {i:ct[i] for i in range(10) if ct[i]>0}

def pq(x,y,xs,ys,cl): # positions x,y, sums xs,ys, clock cl.
    if xs < 5 and ys < 5:
        print(xs,ys)
    if xs >= 21:
        return 1
    elif ys >= 21:
        return 1j
    else:
        if cl==0: # 1,2,3
            return sum([ct[die]*pq(mt(x,die),y,xs+mt(x,die),ys,1-cl) for die in ct]) #die =3 rolls
        if cl==1: # 1,2,3
            return sum([ct[die]*pq(x,mt(y,die),xs,ys+mt(y,die),1-cl) for die in ct]) #die =3 rolls

start = time.time()
z = pq(7,10,0,0,0)
print("p2",int(max(z.imag,z.real)), time.time()-start)
