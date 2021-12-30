def readtimes2(filestring):
    with open(filestring, 'r') as file:
        te, new_cubes, on_off = [x.strip()+',' for x in file.readlines()], [], []
    for li in te:
        nof = {'n':1,'f':0}[li[1]]
        cera = [] # centroid, radius.
        for c in 'xyz':
            xi = li.index(c)
            comi = li.index(',',xi)
            xmi,xma = [int(x)*2 for x in li[xi+2:comi].split('..')[:2]]
            cera.append(((xmi + xma)//2, (xma - xmi)//2))
        new_cubes.append(tuple(cera)) #new cube.
        on_off.append({'n':1,'f':0}[li[1]])
    return new_cubes, on_off

def inr(cl, cr): # intersection of cube-left and cube-right
    for di in zip(cl,cr):
        (mu, rho), (nu, sig)= di
        if abs(mu - nu) > rho + sig:
            return []
    cera = []
    for di in zip(cl,cr):
        (mu, rho), (nu, sig) = di
        xmi = max(mu-rho, nu-sig)
        xma = min(mu+rho, nu+sig)
        cera.append(((xmi + xma)//2, (xma - xmi)//2))
    return tuple(cera)

def vol(cube): # volume. centroid-
    nru = 1
    for di in cube:
        [mu, rho] = di
        nru *= rho+1
    return nru

def ovn(parameter_mi,parameter_ma): # old versus new:
    nc, nf = readtimes2('day22v1.txt')
    ran, cd = [],[] # cd = coverage depth mod2 * 2-1
    for i0 in range(parameter_mi,min(parameter_ma,len(nf))): 
        cl, nof, ran1, cd1 = nc[i0], nf[i0], [], []
        for i in range(len(cd)):
            x = inr(cl,ran[i])
            if x:
                cd1.append({
                    (0,1):0,
                    (0,0):0,
                    (1,1):-1,
                    (-1,1):1,
                    (1,0):-1,
                    (-1,0):1
                    }[(cd[i],nof)])
                ran1.append(x)
        cd.extend(cd1)
        ran.extend(ran1)
        cd.append(nof)
        ran.append(cl)
    return sum([vol(ran[i])*cd[i] for i in range(len(ran)) if cd[i]!=0])

import time
start = time.time()
print("p1:",ovn(0,20))
print("p2:",ovn(0,20)+ovn(20,500), time.time()-start)
