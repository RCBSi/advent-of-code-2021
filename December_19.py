import time
start = time.time()

def dot(u,v):
    return sum([u[i]*v[i] for i in range(len(u))])

def col(x, j):
    return [x[i][j] for i in range(len(x))]

def mm(w,x): #matrix multiplicaiton.
    (n,m) = (range(len(w)), range(len(x[0])))
    return [[dot(w[i],col(x,j)) for j in m] for i in n]

uni = [[[0, 1, 0], [1, 0, 0], [0, 0, -1]], [[1, 0, 0], [0, 0, 1], [0, -1, 0]]] 

for a in uni: # generate the rotations of 3-space preserving {x,y,z,-x,-y,-z}
    for b in uni:
        c = mm(a,b)
        if c not in uni:
            uni.append(c)

def rev(te): # read vectors
    so, soo = [], [] # star-observations per observer.
    for li in te[1:]:
        if ',' in li:
            so.append([int(x) for x in li.split(",")])
        elif li[:12] == '--- scanner ':
            soo.append(so)
            so = []
    soo.append(so)
    return soo

def fi(obl): #fingerprints based on the two nearest stars.
    dps = {}
    for [x,y,z] in obl: 
        dpsx = [[sum([(a-x)**2,(b-y)**2,(c-z)**2]),[a,b,c]] for [a,b,c] in obl]
        dpsx.sort()
        nn2 = [dpsx[i][1] for i in range(1,3)]
        dpnn2 = abs((nn2[0][0]-x)*(nn2[1][0]-x) + (nn2[0][1]-y)*(nn2[1][1]-y) + (nn2[0][2]-z)*(nn2[1][2]-z)) # dot product to the nearest two neighbours. Why not use the function "dot" ? 
        dps[sum([1000000000**i * dpsx[i][0] for i in range(1,3)]) + dpnn2] = [[x,y,z]]+nn2
    return dps

def sams(d1, d2): # if dictionaries d1, d2 contain a common key, 
    for k in d2:
        if k in d1:
            return k
    return None

def gi(i): #guess observation intersections. Use and write to global variables.
    d1 = fi(soo[i])
    for j in range(len(soo)):
        if j not in reached: # fi(soo[i]).keys() & fi(soo[j]).keys()
            d2 = fi(soo[j])
            k = sams(d1,d2)
            if k:
                On[i][j] = [d1[k],d2[k]]
                plan.append([i,j])
                reached.append(j)
                gi(j)

def tr(ob0,ob1,sob):# translate into reference frame ob0 the observations sob made in frame ob1.
    E0 = [[1,0,0],[-1,1,0],[-1,0,1]]
    [M0,M1] = On[ob0][ob1]
    ksx0,ksy0,ksz0 = M0[0]
    ksx1,ksy1,ksz1 = M1[0]
    output = [] 
    for u in uni:
        if mm(E0,M0)[1:] == mm(mm(E0,M1),u)[1:]:
            ru = u # the right u
#    if ru is None: # if we didn't find the right unitary matrix, flip the rows.
#        E1 = mm([[1,0,0],[0,0,1],[0,1,0]], E0)
#        for u in uni:
#            if mm(E1,M0)[1:] == mm(mm(E1,M1),u)[1:]:
#                ru = u # the right u
    for [x,y,z] in sob:
        [[x0,y0,z0]] = mm([[x-ksx1, y-ksy1, z-ksz1]],ru)
        output.append([ksx0+x0,ksy0+y0,ksz0+z0])
    return output

def doit():
    for ob0,ob1 in plan:
        for y in tr(ob0,ob1,soo[ob1]):
            if y not in soo[ob0]:
                soo[ob0].append(y)

with open('day19v1.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]

soo = rev(te)
On =[[ [[],[]] for _ in range(len(soo))] for _ in range(len(soo))]
plan = []
reached = [0]
gi(0)
plan.reverse()
doit()
print("P1",len(soo[plan[-1][0]]))
soo = [[[0,0,0]] for x in soo]
doit()
scanners = soo[plan[-1][0]]
print("part2", max([abs(x-a)+abs(b-y)+abs(c-z) for [a,b,c] in scanners for [x,y,z] in scanners]), time.time() - start)
