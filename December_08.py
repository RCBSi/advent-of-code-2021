def score(u,f):
    [ls,rs] = [u.split()[:10],u.split()[11:15]]
    ls = ["".join(sorted(x)) for x in ls]
    rs = ["".join(sorted(x)) for x in rs]

    con = [(sm,bi) for sm in ls for bi in ls if 
        len(bi) > len(sm) and len(bi)-len(sm) <= 2 and 
        sum([i in bi for i in sm])== len(sm)] # "containment" as a graph.

    nk = {y:0 for y in ls} # number of kids.
    for (x,y) in con:
        nk[y] += 1

    np = {x:0 for x in ls} # number of parents.
    for (x,y) in con:
        np[x] += 1

    winu = {s : f[(nk[s], np[s], len(s))] for s in ls}

    return sum([winu[rs[i]]*(10**(3-i)) for i in range(len(rs))])

with open('day08v1.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]

f ={
    (0, 1, 5): 2,
    (0, 1, 6): 0,
    (0, 2, 2): 1,
    (0, 3, 5): 5,
    (1, 1, 3): 7,
    (1, 1, 4): 4,
    (1, 1, 6): 6,
    (1, 2, 5): 3,
    (3, 1, 6): 9,
    (6, 0, 7): 8}

print(sum([score(u,f) for u in t]))

#import pandas
#d = pd.DataFrame(nk.items(), columns=["id","kids"])
#d["pare"] = d.id.apply(lambda x: np.get(x,-1))
#d["len"] = d.id.apply(lambda x:len(x))
#d.groupby(["kids","pare","len"]).numb.min().to_dict()
#d.numb by hand: 
# 2 has no children and only 8 as a parent; 
# 0 has no children and only 8 as a parent;
# 1 has no children and only 4,7 as parent;
# 5 has no children and 6,8,9 as parents
# 7 has child 1 and parent 3
# 4 has child 1 and parent 9 ...
#Image:
#  1  <  7  <  3  <  9  <  8 
#  1<4<9;  2<5<6;  5<9;  0<8 
