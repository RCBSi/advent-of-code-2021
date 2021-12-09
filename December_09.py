import time
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
    return nout

def is_min(i,j,m,n): # 0 == is not min; n = is min, height = n-1.
    return min([M[i][j] < M[k][l] for (k,l) in ne(i,j,m,n)])*(M[i][j]+1)

def fi(new_value, old_value): # a boolean condition indicating "flows in."
    return new_value < 9 and new_value > old_value

def be(B,M,m,n): # basin-expand:
    P = B #"perimeter"; we could iterate over B each time, too.
    B = []
    while P:
        NP = [(k,l) for (i,j) in P for (k,l) in ne(i,j,m,n) if ((k,l) not in P) and ((k,l) not in B) and fi(M[k][l],M[i][j])]
        for p in P:
            if p not in B:
                B.append(p)
        P = NP
    return B

with open('day09v02.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]

M = [[int(x) for x in u] for u in t if len(u) > 0]
(m,n) = (len(M),len(M[0]))

print("Part1",sum([is_min(i,j,m,n) for i in range(m) for j in range(n)]))

ml = [[(i,j)] for i in range(m) for j in range(n) if is_min(i,j,m,n)]  # minima in a list
start = time.time()
bl = [len(be(b,M,m,n)) for b in ml] # basin length, in a list.
bl.sort()
[x,y,z] = bl[-3:]
print(time.time()-start, "time for Part2:", x*y*z)

# If the condition for accession to a basin: return new_value < 9 and new_value > old_value
# in line 18 were abbreviated to say simply: return new_value < 9
# I would imagine the search to more rapidly and efficiently find the basis. But in fact the runtime would rise from:
# 0.192813873 time for Part2: 8xxxx6
# to 
# 0.778840065 time for Part2: 8xxxx6
