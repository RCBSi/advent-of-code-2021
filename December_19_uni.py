uni1 = [[[0, 1, 0], [1, 0, 0], [0, 0, -1]], [[1, 0, 0], [0, 0, 1], [0, -1, 0]]] # guess 2

for a in uni1: # generate
    for b in uni1:
        c = mm(a,b)
        if c not in uni1:
            uni1.append(c)

uni.sort() 
uni1.sort()
uni == uni1 # check
