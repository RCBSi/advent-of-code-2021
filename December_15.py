import time
def ne(i,j,m,n):
    if i == 0:  # the path gets stuck if it walks "up" the i=0 edge.
        return [(i,j-1),(1,j)]
    if j == 0:
        return [(i-1,j),(i,1)]
    if (i == m-1) or (j == n-1):
        return [(i,j-1),(i-1,j)]
    else:
        return [(i,j-1),(i-1,j),(i,j+1),(i+1,j)]

def ff_init(M): #flow forwards, fill NW to SE.
    ltr = [[M[i][j] for j in range(n)] for i in range(m)]
    ltr[0][0] = 0
    for d in range(1,m+m-1): # do the d-th diagonal.
        if d < m:
            ra = range(d+1)
        else: 
            ra = range(d-m+1,m)
        for k in ra: # 1st coordinate on diagonal m
            l = d - k
            if k == 0:
                try:
                    ltr[k][l] = ltr[k][l-1] + M[k][l]
                except IndexError:
                    print(k,l) 
            elif l == 0:
                try:
                    ltr[k][l] = ltr[k-1][l] + M[k][l]
                except IndexError:
                    print(k,l)
            else: 
                ltr[k][l] = min(ltr[k-1][l],ltr[k][l-1]) + M[k][l]
    return ltr

def ff(l1,M,dir): #flow and fill diagonals to NW or SE.
    ra0 = {'NW':range(m+m-2,0,-1),'SE':range(1,m+m-1)}[dir]
    for d in ra0: # do the d-th diagonal.
        if d < m:
            ra1 = range(d+1)
        else: 
            ra1 = range(d-m+1,m)
        for k in ra1: # 1st coordinate on diagonal m
            l = d - k
            nel = ne(k,l,m,n)
            l1[k][l] = min([l1[i][j]+ M[k][l] for (i,j) in ne(k,d-k,m,n)])
    return ltr

st = time.time()
with open('day15v1.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]

(m,n) = (len(te), len(te[0]))
(m0,n0) = (len(te), len(te[0]))
M = [[int(x) for x in u] for u in te]
print("P1",ff_init(M)[m-1][n-1]) # In my problem text, at least one minimal path was monotonically NW-to-SE, so no ff was needed. If this is too high; run line 73 a few times.
mult = 5
M2 = [[0 for i in range(n0*mult)] for j in range(m0*mult)]
for i in range(mult):
    for j in range(mult):
        for k in range(n0):
            for l in range(m0):
                M2[m0*i+k][n0*j+l] = (M[k][l]+i+j-1)%9+1
        
(m,n) = (len(te)*mult,len(te[0])*mult)
M = M2
ltr = ff_init(M)
result = ltr[m-1][n-1]
last_result = result + 1
while result < last_result: # This should loop at most (9-1)/2 times, since every SE-to-NW step costs at least 1 move up and 1 move down, and avoids a barrier with a cost at most 9.
    last_result = result
    print(time.time() - st, result)
    ltr = ff(ff(ltr,M,'SE'),M,'NW')
    result = ltr[m-1][n-1]
print("P2")
