import time
start = time.time()

def tou(loc,t): # touched -- step t touched location loc.
    out = True
    for i in range(3):
        out = out & (loc[i] in ran[t][i])
    return out

def lt(loc, initleng): # for a location, the last time touched during initialization.
    ts = [tou(loc,t) for t in range(initleng-1,-1,-1)]
    if True in ts:
        return initleng-1 - ts.index(True)
    return None

def crazy_core(cutoff):
    ct = 0
    for x in range(-50,51):
        if x%17:
            print(x)
        for y in range(-50,51):
            for z in range(-50,51):
                ti = lt([x,y,z], cutoff)
                if ti is not None:
    #                print((x,y,z), ti, oof[ti])
                    ct += oof[ti]
    return ct

def linin(ra,rb): #detect lineaer intersection between two ranges; if they intersect, return three ranges with the same span and no intersection.
    if min(ra) in rb:
        return range(min(rb),min(ra)), range(min(ra),min(max(ra)+1,max(rb)+1)), range(min(max(ra)+1,max(rb)+1),max(max(ra)+1,max(rb)+1))
    if min(rb) in ra:
        return linin(rb,ra)
    return []

def ovl(i,j): # is there overlap?
    if i==j:
        return False  
#    if va[i] == 0:
#        return False
#    if va[j] == 0:
#        return False
#    if oof[i] == 0 and oof[j] == 0:
#        return False # We don't care about intersections of off instructions with each other.
    return all([linin(ran[i][k],ran[j][k]) for k in range(3)])

def ovll(i,j): # is there overlap?
    try:
        return [linin(ran[i][k],ran[j][k]) for k in range(3)]
    except IndexError:
        print("ovll failed at",i,j)

def adcu(i,j): # turn off the validity of these and 
    if ran[i] == ran[j]:
        if ex[i] < ex[j]:
            va[i] = 0
        if ex[j] < ex[i]:
            va[j] = 0
    else:
        va[i] = 0
        va[j] = 0
        shatter(i,j)

def first_intersection(i,j):
    while 1:
        if ovl(i,j): # if the cubes overlap,
            adcu(i,j) # add cubes.

        if i==len(ran)-1 and j == len(ran)-1:
            return 1
        elif j == len(ran)-1:
            if 1 in va[i+1:]:
                i = va.index(1,i+1)
            if i%101==0:
                print(i,"<",len(ran), round(time.time()-start))
            j=0
        else:
            if 1 in va[j+1:]:
                j = va.index(1,j+1)
            else:
                j=len(va)-1

def insect(i,j): # the intersection of i and j.
    rm = ovll(i,j)
    for a in rm[0]: 
        for b in rm[1]:
            for c in rm[2]:                
                if len(a) == 0 or len(b) == 0 or len(c) == 0:
                    1
                else:
                    pt = [min(a),min(b),min(c)]
                    if tou(pt,j) and tou(pt,i):
                        return len(a)*len(b)*len(c)

def insect_effect(cutoff):
    inse_double, inse_covered = 0,0
    for i in range(cutoff,len(te)-1):
        if i%3 == 0:
            print("IE:",i)
        for j in range(i+1,len(te)):
            if ovl(i,j):
                try:
                    r3, pa = insect(i,j)
                except TypeError:
                    print("HCF_insect_effect",i,j)
                [a,b,c] = r3
                q,r = pa
                if (q,r) == (1,0):
                    inse_covered += len(a)*len(b)*len(c)
                if (q,r) == (1,1):
                    inse_double += len(a)*len(b)*len(c)
    return inse_double, inse_covered

def insect_effect_faster(cutoff):
    inse_double, inse_covered = 0,0
    for i in range(cutoff,len(te)-1):
        if oof[i] == 1:
            if i%3 == 0:
                print("IE:",i)
            for j in range(i+1,len(te)):
                if ovl(i,j):
                    ins = insect(i,j)
                    if oof[j] == 1:
                        inse_double += ins
                    if oof[j] == 0:
                        inse_covered += ins
    return inse_double, inse_covered

def main_sequence_stars(cutoff):
    mss = 0
    for i in range(cutoff,len(te)-1):
        [a,b,c] = ran[i]
        mss += len(a)*len(b)*len(c)*oof[i]
    return mss

def shatter(i,j): 
    if ex[i] == ex[j]:
        print("We did not expect to handle overlap from shards of the same shattered cube.")
    if ex[j] < ex[i]:
        return shatter(j,i)
    # Now we may assume that ex[i] < ex[j], that j dominates i.
    rm = ovll(i,j)
    for a in rm[0]: 
        for b in rm[1]:
            for c in rm[2]:
                if len(a) == 0 or len(b) == 0 or len(c) == 0:
                    1
                elif tou([min(a),min(b),min(c)],j):
                    ran.append([a,b,c])
                    oof.append(oof[j])
                    va.append(1)
                    ex.append(ex[j])
                elif tou([min(a),min(b),min(c)],i):
                    ran.append([a,b,c])
                    oof.append(oof[i])
                    va.append(1)
                    ex.append(ex[i])

def slow_false():
    cutoffth = 10
    cc = crazy_core(cutoffth)
    print("crazy_core",cc)
    mss = main_sequence_stars(cutoffth)
    print("main_sequence_stars",mss)
    i1, l2 = insect_effect_faster(cutoffth)
    print("pt2", ms - i1 - i2 + cc, i1, l2)

####################

def isin(p,ra3): # touched -- step t touched location loc.
    out = [(p[k] in ra3[k]) for k in range(3)]
    return all(out)

def ove(ra3,rb3): # 3 ranges x3 ranges => 27 ranges.
    out = [linin(ra3[k],rb3[k]) for k in range(3)]
    if all(out):
        return out

def ter(ra3,rb3): # one of those 27 is the intersection.
    rm = ove(ra3,rb3)
    for a in rm[0]: 
        for b in rm[1]:
            for c in rm[2]:
                if len(a) == 0 or len(b) == 0 or len(c) == 0:
                    1
                else:
                    pt = [min(a),min(b),min(c)]
                    if isin(pt,ra3) and isin(pt,rb3):
                        return a,b,c

def run_and_measure(mi,ma):
    for i in range(mi,min(ma,len(te))): #range(len(te)):
        if i%5 == 0:
            print(i, len(ran))
        li = te[i]
        xi = li.index('x=')
        yi = li.index('y=')
        zi = li.index('z=')
        xmi,xma = [int(x) for x in li[xi+2:yi-1].split('..')[:2]]
        ymi,yma = [int(y) for y in li[yi+2:zi-1].split('..')[:2]]
        zmi,zma = [int(z) for z in li[zi+2:].split('..')[:2]]    
        ra3 = [range(xmi,xma+1), range(ymi,yma+1), range(zmi,zma+1)]
        nof = {'n':1,'f':0}[li[1]]
        for i in range(len(ran)):
            if ove(ra3,ran[i]):
                ran.append(ter(ra3,ran[i]))
                oof.append(nof)
                cd.append({(0,1):0,(0,0):0,(1,1):-1,(-1,1):1,(1,0):-1,(-1,0):1}[(cd[i],nof)])
        ran.append(ra3)
        oof.append(nof)
        cd.append(nof)

with open('day22v1.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]
    oof, ran, cd = [],[],[] # on-off, ranges, coverdepth.

run_and_measure(0,20)
vol = [len(ran[i][0])*len(ran[i][1])*len(ran[i][2]) for i in range(len(ran))] 
pt2core = sum([vol[i]*cd[i] for i in range(len(ran))])
print("p2:", sum([vol[i]*cd[i] for i in range(len(ran))]))
oof, ran, cd = [],[],[] # on-off, ranges, coverdepth.
run_and_measure(20,500)
vol = [len(ran[i][0])*len(ran[i][1])*len(ran[i][2]) for i in range(len(ran))] 
print("p2:", sum([vol[i]*cd[i] for i in range(len(ran))])+pt2core)


results = '''
Output tracks how many cuboids were part of the sum:
0 0
5 23
10 575
15 2431
p2: 648023
20 0
25 5
30 10
35 17
40 24
45 32
50 41
55 46
60 54
65 62
70 70
75 84
80 93
85 111
90 121
95 131
100 156
105 193
110 214
115 232
120 255
125 275
130 299
135 337
140 361
145 406
150 444
155 474
160 532
165 563
170 578
175 625
180 666
185 695
190 713
195 775
200 859
205 887
210 934
215 985
220 1081
225 1159
230 1193
235 1325
240 1408
245 1493
250 1724
255 1833
260 2137
265 2509
270 2553
275 2734
280 2802
285 2896
290 3058
295 3122
300 3176
305 3294
310 3401
315 3464
320 3571
325 3824
330 3938
335 3997
340 4164
345 4379
350 4745
355 5163
360 5352
365 5595
370 6063
375 6200
380 6663
385 7367
390 7550
395 7654
400 8130
405 8371
410 8751
415 8904
p2: 1285677377200526+ 648023 = 1285677377848549


Output on the test case:
0 0
5 16
p2: 474140
10 0
15 8
20 19
25 54
30 116
35 196
40 360
45 811
50 2612
55 4333
p2: 2758514935808095
2758514935808095+474140
2758514936282235
'''
