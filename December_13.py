def fl(x,y): # flip x over y. Fix y.
    if x <= y:
        return x
    else:
        return 2*y - x

def stat(pl): # where are these points? 
    xl,yl = [],[]
    for (x,y) in pl:
        xl.append(int(x))
        yl.append(int(y))
    return min(xl),max(xl), min(yl), max(yl), range(max(xl)+1), range(max(yl)+1)

def fo(pl,ti): # folding operation on point list, text instruction.
    print(len(pl),ti[11:])
    if ti[11] == 'y':
        return [(y,x) for (x,y) in fo([(y,x) for (x,y) in pl],'fold along x'+ti[12:])]
    elif ti[11] == 'x':
        cl = int(ti[13:]) #cut line
        return [(fl(x,cl),y) for (x,y) in pl]
    else: 
        print("cannot fold!", ti, stat(pl))

with open('doy13v2.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]

pl = []# point list
for u in te[:-13]: # change this and line 32: u in points, ft "flip-text" in instructions.
    (x,y) = u.split(',')
    pl.append((int(x), int(y)))

for ft in te[-12:]: # change this to include all the instructions: -3 test; -13 real.
    pl = fo(pl,ft) #for part 1 just do this once, for the first instruction te[-12]

[xr,yr] = stat(pl)[-2:]
M = [[0 for x in xr] for y in yr]

for (x,y) in fo(pl,te[-12]):
    try:
        M[y][x] = 1
    except IndexError: print(x,y,stats(pl))

print(sum([sum(row) for row in M]), "part 2:") 
[print("".join([{0:'.', 1:'#'}[p] for p in row])) for row in M]
