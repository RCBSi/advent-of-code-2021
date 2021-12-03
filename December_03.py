#spaghetti 
with open('day03v1.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]

m = len(t[0])
tots = {n:0 for n in range(m)}
for u in t:
    for n in range(m):
        tots[n] += int(u[n])

gamma_b = [tots[n] > len(t)//2 for n in range(m)]
epsilon_b = [tots[n] < len(t)//2 for n in range(m)]
(g,e) = (0,0)
for n in range(m):
    g += 2**(m-n-1)*gamma_b[n]
    e += 2**(m-n-1)*epsilon_b[n]

print("Part1:", g*e)

fo = {u:1 for u in t} #filtered, ok for oxygen

for i in range(m):
    bco = {} #bit criteria for oxygen
    ct = 0

    for u in fo:
        if fo[u] == 1:
            bco[u] = int(u[i])
            ct += 1

    f1 = int(sum(bco.values()) >= ct/2) #filter

    for k in fo: 
        if k[i] == str(1-f1):
            fo[k] = 0
#    print("i ", i, "ct ", ct, "filter-bit", f1, "range ", fo)
    
for k in fo: 
    if fo[k] == 1:
        ox = 0
        for n in range(m):
            ox += 2**(m-n-1) *int(k[n])

fc = {u:1 for u in t} #filtered, ok for carbon monoxide

i = 0
while ct > 1:
    bcc = {} #bit criteria for carbon monoxide
    ct = 0

    for u in fc:
        if fc[u] == 1:
            bcc[u] = int(u[i])
            ct += 1

    f1 = int(sum(bcc.values()) < ct/2) #filter

    ct = 0
    for k in bcc:
        if k[i] == str(1-f1):
            fc[k] = 0
        else:
            ct += 1
#    print("i ", i, "ct ", ct, "filter-bit", f1, "range ", fc)
    i += 1
    
oc = 0
for k in fc: 
    if fc[k] == 1:
        for n in range(m):
            oc += 2**(m-n-1) *int(k[n])

print("Part2:", ox, oc, ox*oc)
