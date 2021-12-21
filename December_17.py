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
