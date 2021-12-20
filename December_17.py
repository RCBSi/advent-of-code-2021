def lv(v): #limiting height of y with velocity v; lim val of x with velocity v. 
    return v*(v+1)//2

with open('day17v0.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]
    xmin, xmax = [int(x) for x in te[0][te[0].index('x')+2:te[0].index(','):].split('..')]

    ymin, ymax = [int(x) for x in te[0][te[0].index('y')+2:].split('..')]

if [x for x in range(0,xmax) if xmin < lv(x) and lv(x) < xmax]: # If we can limit to the x-target, 
    print("pt1",lv(ymin)) # Launch at v = -ymin+1; rise lv(v); fall lv(v); return to 0; velocity is ymin. next step in target.

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
ry = [y for y in range(ymin, -1*ymin+1)]
rx = [x for x in range([lv(k) >= xmin for k in range(20)].index(True),xmax+1) if xmin <= lv(x) and x <= xmax]
print("pt2",sum([1 for x in rx for y in ry if fh(x,y,tx,ty) >= ymin]))
