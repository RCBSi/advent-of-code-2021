def score(u):
    [ls,rs] = [u.split()[:10],u.split()[11:15]]
    ls = ["".join(sorted(x)) for x in ls]
    rs = ["".join(sorted(x)) for x in rs]

    con = [(sm,bi) for sm in ls for bi in ls if 
        len(bi) > len(sm) and len(bi)-len(sm) <= 2 and 
        sum([i in bi for i in sm])== len(sm)] # "containment" 

    num_kids = {y:0 for y in ls} 
    for (x,y) in con:
        num_kids[y] += 1

    num_pare = {x:0 for x in ls} #parents
    for (x,y) in con:
        num_pare[x] += 1

    lenu = {2:1,4:4,3:7,7:8} # le = length; wi = wirset; nu = number.
    winu = {s:lenu[len(s)] for s in ls if len(s) in lenu} 
    winu[[s for s in ls if len(s) == 6 and num_kids[s] == 0][0]] = 0
    winu[[s for s in ls if len(s) == 5 and num_pare[s] == 1][0]] = 2
    winu[[j for (i,j) in con if len(i) == 3][0]] = 3     
    winu[[s for s in ls if len(s) == 5 and num_pare[s] == 3][0]] = 5
    winu[[s for s in ls if len(s) == 6 and num_kids[s] == 1][0]] = 6   
    winu[[j for (i,j) in con if len(i) == 4][0]] = 9

    return sum([winu[rs[i]]*(10**(3-i)) for i in range(len(rs))])

with open('day08v1.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]

print(sum([score(u) for u in t]))
