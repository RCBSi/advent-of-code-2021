# decouple x and y. Calculate highest y that passes through the range.

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

def lv(v): #limiting height of y with velocity v; lim val of x with velocity v. Should calculate the answer.
    return v*(v+1)//2

tx = range(34,67+1) # target area x, read it from the input.
ty = range(-215,-186+1) # target area y.

p1 = max([fh(x,y,tx,ty) for y in range(0,217) for x in range(8,68)]) # lv(8) in tx, sigh. Clearly ivx = 68 overshoots. velocity 217 upwards returns to y=0 with velocity -217, which clearly overshoots.
p2 = sum([1 for y in range(-217,217) for x in range(8,68) if fh(x,y,tx,ty) > -216]) # Clearly, velocity ivy = -217 overshoots. Likwise +217 returns to y=0 with velocity -217.

print("Part1:", p1)
print("Part2:", p2)

# Did not compute. Search was fast enough.

