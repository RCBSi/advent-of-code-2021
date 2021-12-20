uni = [ #these are the rotations of 3-space preserving {x,y,z,-x,-y,-z}
    [[-1, 0, 0], [0, -1, 0], [0, 0, 1]],
    [[-1, 0, 0], [0, 0, -1], [0, -1, 0]],
    [[-1, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[-1, 0, 0], [0, 1, 0], [0, 0, -1]],
    [[0, -1, 0], [-1, 0, 0], [0, 0, -1]],
    [[0, -1, 0], [0, 0, -1], [1, 0, 0]],
    [[0, -1, 0], [0, 0, 1], [-1, 0, 0]],
    [[0, -1, 0], [1, 0, 0], [0, 0, 1]],
    [[0, 0, -1], [-1, 0, 0], [0, 1, 0]],
    [[0, 0, -1], [0, -1, 0], [-1, 0, 0]],
    [[0, 0, -1], [0, 1, 0], [1, 0, 0]],
    [[0, 0, -1], [1, 0, 0], [0, -1, 0]],
    [[0, 0, 1], [-1, 0, 0], [0, -1, 0]],
    [[0, 0, 1], [0, -1, 0], [1, 0, 0]],
    [[0, 0, 1], [0, 1, 0], [-1, 0, 0]],
    [[0, 0, 1], [1, 0, 0], [0, 1, 0]],
    [[0, 1, 0], [-1, 0, 0], [0, 0, 1]],
    [[0, 1, 0], [0, 0, -1], [-1, 0, 0]],
    [[0, 1, 0], [0, 0, 1], [1, 0, 0]],
    [[0, 1, 0], [1, 0, 0], [0, 0, -1]],
    [[1, 0, 0], [0, -1, 0], [0, 0, -1]],
    [[1, 0, 0], [0, 0, -1], [0, 1, 0]],
    [[1, 0, 0], [0, 0, 1], [0, -1, 0]],
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]]

def dot(u,v):
    return sum([u[i]*v[i] for i in range(len(u))])

def col(x, j):
    return [x[i][j] for i in range(len(x))]

def mm(w,x): #matrix multiplicaiton.
    (n,m) = (range(len(w)), range(len(x[0])))
    return [[dot(w[i],col(x,j)) for j in m] for i in n]

def rev(te): # read scanner-beacon vectors. 
    so = [] # star-observation, a list of stars, indexed by observer-number.
    soo = [] # a list of lists of star-observations.
    for li in te:
        if len(li) == 0:
            soo.append(so)
        elif li[:12] == '--- scanner ':
            so = []
        else:
            os = [int(x) for x in li.split(",")] # vector from observer to star.
            so.append(os)
    soo.append(so)
    return soo

def fi(obl): #fingerprints based on the two nearest stars.
    dps = {}
    for [x,y,z] in obl: 
        dpsx = [sum([(a-x)**2,(b-y)**2,(c-z)**2]) for [a,b,c] in obl]
        dpsx.sort()
        nn2 = [[a,b,c] for [a,b,c] in obl if sum([(a-x)**2,(b-y)**2,(c-z)**2]) == dpsx[1]]+[
            [a,b,c] for [a,b,c] in obl if sum([(a-x)**2,(b-y)**2,(c-z)**2]) == dpsx[2]
        ]
        dpnn2 = abs((nn2[0][0]-x)*(nn2[1][0]-x) + (nn2[0][1]-y)*(nn2[1][1]-y) + (nn2[0][2]-z)*(nn2[1][2]-z)) # dot product to the nearest two neighbours. Why not use the function "dot" ? 
        dps[sum([10000000**i * dpsx[i] for i in range(1,3)])*10000000 + dpnn2] = [[x,y,z]]+nn2
    return dps

def gi(soo): # guess intersections.
    M = [[0 for _ in range(len(soo))] for _ in range(len(soo))]
    On =[[ [[],[]] for _ in range(len(soo))] for _ in range(len(soo))]
    pairs = []
    for i in range(len(soo)):
        di = fi(soo[i])
        for j in range(i+1,len(soo)):#  fi(soo[i]).keys() & fi(soo[j]).keys()
            ct = 0
            d2 = fi(soo[j])
            for k in d2:
                if k in di:
                    ct += 1
                    out = [di[k],d2[k]]
            M[i][j] = ct
            if ct >= 1:
                On[i][j] = out
                On[j][i] = [out[1],out[0]]
                pairs.append([i,j])
    return M, On, pairs

def tr(ob0,ob1,sob):# translate into reference frame ob0 the observations sob made in frame ob1.
    E0 = [[1,0,0],[-1,1,0],[-1,0,1]]
    [M0,M1] = On[ob0][ob1]
    ksx0,ksy0,ksz0 = M0[0]
    ksx1,ksy1,ksz1 = M1[0]
    output = [] 
    for u in uni:
        if mm(E0,M0)[1:] == mm(mm(E0,M1),u)[1:]:
            ru = u # the right u
    if ru is None: # if we didn't find the right unitary matrix, flip the rows.
        E1 = mm([[1,0,0],[0,0,1],[0,1,0]], E0)
        for u in uni:
            if mm(E1,M0)[1:] == mm(mm(E1,M1),u)[1:]:
                ru = u # the right u
    for [x,y,z] in sob:
        [[x0,y0,z0]] = mm([[x-ksx1, y-ksy1, z-ksz1]],ru)
        output.append([ksx0+x0,ksy0+y0,ksz0+z0])
    return output

def rp(Pg): #from the graph Pg, make a reduction plan. 
    planned = {}
    plan = []
    nn = {i:[] for i in range(len(soo)) if i not in planned}
    for [x,y] in Pg:
        if x not in planned and y not in planned:
            nn[x].append(y)
        if y not in planned and x not in planned:
            nn[y].append(x)
    len_queue = [(len(nn[k]),len(soo)-k) for k in nn]
    len_queue.sort()
    while len(len_queue) > 1:
        plan_me = len(soo)-len_queue[0][1]
        planned[plan_me] = 1
        plan.append([plan_me,nn[plan_me][0]])
        nn = {i:[] for i in range(len(soo)) if i not in planned}
        for [x,y] in Pg:
            if x not in planned and y not in planned:
                nn[x].append(y)
            if y not in planned and x not in planned:
                nn[y].append(x)
        len_queue = [(len(nn[k]),len(soo)-k) for k in nn]
        len_queue.sort()
    return plan

with open('day19v0.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]

soo = rev(te)
M, On, Pg = gi(soo)
[print(".".join([str(x) for x in row])) for row in M]

so1 = [[y for y in x] for x in soo]
plan = rp(Pg)

for ob1,ob0 in plan:
    for y in tr(ob0,ob1,so1[ob1]):
        if y not in so1[ob0]:
            so1[ob0].append(y)

print("P1",len(so1[plan[-1][1]]))

so1 = [[[0,0,0]] for x in soo]

for ob1,ob0 in plan:
    for y in tr(ob0,ob1,so1[ob1]):
        if y not in so1[ob0]:
            so1[ob0].append(y)

scanners = so1[plan[-1][1]]

dmax = 0
for [x,y,z] in scanners:
    for [a,b,c] in scanners:
        dmax = max(abs(x-a)+abs(b-y)+abs(c-z), dmax)

print("part2", dmax)
