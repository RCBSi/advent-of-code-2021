with open('doy14v1.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]

st = te[0]

tr = {}
for u in te[2:]:
    (a,b) = u.split(" -> ")
    tr[a] = b
#    print(a,b)

def ins(st): # insert into the string.
    out = st[0]
    for i in range(len(st)-1):
        if st[i:i+2] in tr:
            out += tr[st[i:i+2]]
            out += st[i+1]
    return out

def ud(pc): #update pair-count.
    npc = {el+el2:0 for el in me for el2 in me}
    for p in pc:
        (a,b) = (p[0],p[1])
        c = tr[p]
        npc[a+c]+= pc[a+b]
        npc[c+b]+= pc[a+b]
    return npc

def ip(st): #initialize paircount
    npc = {el+el2:0 for el in me for el2 in me}
    for i in range(len(st)-1):
        npc[st[i:i+2]] += 1
    return npc

def sc(pc,el): # single-character count.
    return sum([pc[el + x] for x in me])+{True:1, False:0}[st[-1]==el]

me = {el:0 for el in ['B', 'C', 'F', 'H', 'K', 'N', 'O', 'P', 'S', 'V']} # mendeleev table of elements.
pc = ip(st)
for _ in range(40):
    pc = ud(pc)
    cts = [sc(pc,x) for x in me]
    print(cts)
    print(_, max(cts) - min(cts))

for _ in range(14):
    st = ins(st)
    cts = [st.count(el) for el in me]
    print(_, max(cts) - min(cts))


