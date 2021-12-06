def av (sf, ct2, x,y): #add vent
    if sf[x][y] == 1: #count squares where ventlines overlap.
        ct2 += 1
    sf[x][y] += 1
    return (sf, ct2)

with open('day05v1.txt', 'r') as file:
    t = {x.strip():0 for x in file.readlines()}

(n, ct2) = (1000, 0) # ct2 = count 2's . ct2 for part 2
sf = [[0 for i in range(n)] for j in range(n)] # seafloor
for u in t:
    [[a,b],[c,d]] = [[int(y) for y in x.split(",")] for x in u.split(" -> ")]
    if a==c: # vertical 
        [b,d] = [min(b,d),max(b,d)]
        for y in range(b,d+1):
            (sf, ct2) = av(sf,ct2,y,a)
    elif b==d: # horizontal
        [a,c] = [min(a,c),max(a,c)]
        for y in range(a,c+1):
            (sf, ct2) = av(sf,ct2,b,y)
    elif (a<c) == (b<d): #slope=1
        [b,d] = [min(b,d),max(b,d)]
        [a,c] = [min(a,c),max(a,c)]
        vl = d-b+1 # ventline length
        for i in range(vl):
            (sf, ct2) = av(sf,ct2,b+i,a+i)
    else: # slope negative 1 diagonal
        [b,d] = [min(b,d),max(b,d)]
        [a,c] = [min(a,c),max(a,c)]
        vl = d-b+1 # ventline length
        for i in range(vl):
            (sf, ct2) = av(sf,ct2,b+i,c-i)

print("Answer:", ct2)
# for part 1, commment/cut from "elif (a<c) == (b<d):" to the end.
