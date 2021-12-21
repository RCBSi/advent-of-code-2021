import time
start = time.time()

def hit(y,t,ymin,ymax): 
    yt = sum(range(y,y-t,-1))
    return yt in range(ymin, ymax+1)

def hitlate(y,ymin,ymax): 
    yt, dy = 0, y
    for t in range(-ymin*3):
        yt+= dy
        dy -= 1
        if (yt in range(ymin, ymax+1)):
            return t
        if yt < ymin:
            return -1

def hitx(x,t,xmin,xmax): 
    minimum_velocity = 0
    xt = sum(range(x,max(x-t,minimum_velocity),-1))
    return xt in range(xmin, xmax+1)

def t_to_y(t, ymin, ymax):
    return [y for y in range(ymin,-ymin) if hit(y,t,ymin,ymax)]

def t_to_x(t, xmin, xmax):
    return [x for x in range(-ymin) if hitx(x,t,xmin,xmax)]
    
with open('day17v1.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]
    xmin, xmax = [int(x) for x in te[0][te[0].index('x')+2:te[0].index(','):].split('..')]
    ymin, ymax = [int(x) for x in te[0][te[0].index('y')+2:].split('..')]

if t_to_x(-ymin*3,xmin,xmax):
    print("pt1",ymin*(ymin+1)//2) 

cut, count, ctseq = 0, 0, []
while t_to_x(cut,xmin,xmax) != t_to_x(cut+1,xmin,xmax):
    a,b = len(t_to_x(cut,xmin,xmax)),len(t_to_y(cut,ymin,ymax))
    count += a*b
    ctseq.append((a,b))
    cut += 1

low = sum([a*b for (a,b) in ctseq])
print(time.time()-start)
slow = len([y for y in range(ymin,-ymin) if hitlate(y,ymin,ymax)+1>=cut])
patient = len(t_to_x(cut,xmin,xmax))
print("p2",low + slow*patient, "=", low,"+", slow,"*",patient, time.time()-start)

def st(x,y,xv,yv): # step
    x+= xv
    y+= yv
    if xv > 0:
        xv -= 1
    if xv < 0:
        xv += 1
    yv += -1
    return x,y,xv,yv

def fh(ivx,ivy,tx,ty): #find highest point
    vx, vy = (ivx,ivy)
    ymax = 0
    (x,y) = (0,0)
    while y >= -215: 
        (x,y,vx,vy) = st(x,y,vx,vy)
        if y > ymax:
            ymax = y
        if (x in tx) and (y in ty):
            return ymax
    return y

tx = range(xmin,xmax+1) # target area x, read it from the input.
ty = range(ymin,ymax+1) # target area y.
ry = range(ymin, -ymin+1)
rx = range(0,xmax+1)
print("pt2",sum([1 for x in rx for y in ry if fh(x,y,tx,ty) >= ymin]), time.time()-start)

# The answers agree on target area: x=34..67, y=-215..-186
# Answers don't match: target area: x=30..60, y=-210..-180
# The brute count is of course correct. 
