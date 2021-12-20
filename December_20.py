def rem(M,ov,i,j): #read the matrix or take the outside value
    if i in range(len(M)) and j in range(len(M)):
        return M[i][j]
    else:
        return ov

def gal(b, M,i,j): #game of life; bitstring M, matrix M, location i,j.
    bl = [rem(M,ov,k,l) for k in range(i-1,i+2) for l in range(j-1,j+2)]
    lu = int(''.join('01'[i] for i in bl), 2)
    return b[lu]

def gali(b,M,ov): # game of life for the whole matrix.
    return [[gal(imea,M,i-1,j-1) for j in range(len(M)+2)] for i in range(0,len(M)+2)], {0:imea[0], 1:imea[511]}[ov]

with open('day20v1.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]

imea = [{'#':1, '.':0}[x] for x in te[0]] # image enhancement algorithm, i.e., our variation on the game of life rules.

M = [[{'#':1, '.':0}[x] for x in u] for u in te[2:]]
ov = 0 # outside value.
#[print("".join([str(x) for x in row])) for row in M]

for _ in range(2):
    M, ov = gali(imea, M, ov)
#    [print("".join([{1:'#', 0:'.'}[x] for x in row])) for row in M]

print("p1",sum([sum(r) for r in M]))

for _ in range(50-2):
    M, ov = gali(imea, M, ov)
#    [print("".join([{1:'#', 0:'.'}[x] for x in row])) for row in M]

print("p2",sum([sum(r) for r in M]))
