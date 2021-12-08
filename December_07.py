import numpy 
def cost(x,y): # L2-norm is minimized at the average.
    (x,y) = (min(x,y),max(x,y))
    return (y-x+1)*(y-x)//2

with open('day07v1.txt', 'r') as file:
    t0 = [x.strip() for x in file.readlines()]
    t = [int(x) for x in t0[0].split(',')]

(x,z) = (int(numpy.median(t)), int(numpy.average(t)))

print("Part1:", x, sum([abs(y-x) for y in t]))

cs = {sum([cost(w,y) for y in t]):w for w in range(z-2,z+2)} # ah, test it.
if cs[min(cs)] == z:
    print("Part2:", z, sum([cost(z,y) for y in t]))
