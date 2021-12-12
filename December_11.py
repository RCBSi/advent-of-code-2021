def ne(i,j,m,n): # neighbors
    nout = []
    if i > 0:
        nout.append([i-1,j])
    if i < m-1:
        nout.append([i+1,j])
    if j > 0:
        nout.append([i,j-1])
    if j < n-1:
        nout.append([i,j+1]) 
    if i > 0 and j > 0:
        nout.append([i-1,j-1])
    if i > 0 and j < n-1:
        nout.append([i-1,j+1])
    if i < m-1 and j > 0:
        nout.append([i+1,j-1])
    if i < m-1 and j < n-1:
        nout.append([i+1,j+1])
    return nout

def fl(M): # flashers' lastest newly retriggered batch.
    return {(i,j):0 for i in range(m) for j in range(n) if M[i][j] > 9 and M[i][j] < 20}

def di(M): # We who are about to die salut you.
    return {(i,j):0 for i in range(m) for j in range(n) if M[i][j] > 9}

def up(M,i,j): # update pixel.
    el = sum([1 for (k,l) in ne(i,j,len(M),len(M[0])) if (k,l) in fl(M)])
    if (i,j) in fl(M):
        return M[i][j] + 20
    else: 
        return M[i][j] + el

def down(M,i,j): #downdate pixel.
    if (i,j) in di(M):
        return 0
    else:
        return M[i][j]

def us(M): #update step
    M = [[M[i][j]+1 for j in range(n)] for i in range(m)]
    while len(fl(M)) > 0: #contagion > flashmob 
        M = [[up(M,i,j) for j in range(n)] for i in range(m)]
    sc = len(di(M))
    M = [[down(M,i,j) for j in range(n)] for i in range(m)]
    return M,sc

with open('day11v0.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]

M = [[int(x) for x in u] for u in t if len(u) > 0]
(m,n) = (len(M),len(M[0]))
ct = 0
for i in range(100):
    (M,ctd) = us(M)
    ct += ctd

while sum([sum(row) for row in M]) > 0:
    (M,ctd) = us(M)
    i+= 1

print("Part1:", ct)
print("Part2:", i+1)

