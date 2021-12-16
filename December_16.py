hexdict = '''0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111'''

hd = {} # hex dictionary
for x in hexdict.split('\n'):
    (a,b) = x.split(' = ')
    hd[a] = [int(bi) for bi in list(b)]

def bi(bitlist): # binary to decimal integer.
    bs = [int(x) for x in bitlist]
    bs.reverse()
    pt,integerout = 1,0
    for b in bs:
        integerout += b*pt
        pt *= 2
    return integerout

def rp(bitlist,pt): # read a packet from the bit transmission at the pointer.

    bt = [int(x) for x in bitlist]
    la = ['V']*3 # labels.
    p1 = pt
    vn = bt[p1:p1+3] #version number
    p1 += 3
    la += ['T']*3
    tn = bt[p1:p1+3] # type number 
    p1 += 3  
    if tn == [1,0,0]: # Type = "literal"
        cob = bt[p1] #"continue" bit cob==0 iff stop.
        la += ['C']+['A']*4
        lnb = bt[p1+1:p1+5] # literal number, binary 
        p1 += 5
        while cob:
            cob = bt[p1]
            la += ['C']+['A']*4
            lnb += bt[p1+1:p1+5]
            p1 += 5
        return None, None, p1, bi(lnb), bi(vn), bi(tn), "".join(la)

    if tn != [1,0,0]: # type "operator"
        lt = bt[p1] # llength typpe
        p1 += 1
        la += ['I']
        if lt==0:
            la += ['L']*15
            le = bi(bt[p1:p1+15])
            p1 += 15
            return None,le,p1, None, bi(vn), bi(tn), "".join(la)
        if lt:
            la += ['L']*11
            le = bi(bt[p1:p1+11])
            p1 += 11
            return le,None, p1, None, bi(vn), bi(tn), "".join(la)

def evp(bt,pt): # extract values from a packet to arbitrary depth.
    (nl, ll, ap, ov, vn, tn, labels) = rp(bt,pt)
    val_list = []
    ap_list = []
    if ll:
        ap0 = ap
        while ap0 < ap+ll:
            ovi,apmax = evp(bt,ap0)
            (nl0, ll0, ap0, ov0, vn0, tn0, labels) = rp(bt,ap0)
            ap0 = apmax
            val_list.append(ovi)
            ap_list.append(apmax)
    if nl:
        ap0 = ap
        for dummy in range(nl):
            ovi, apmax = evp(bt,ap0)
            (nl0, ll0, ap0, ov0, vn0, tn0, labels) = rp(bt,ap0)
            ap0 = apmax
            val_list.append(ovi)
            ap_list.append(apmax)
    if ov is not None and not val_list: 
        return ov, ap
    if val_list and ov is None:
        v = red(val_list, tn) 
        return v, max(ap_list) # to see the nested values, return val_list

def red(lv, tn): #reduce..
    if tn == 0:
        return sum(lv)
    if tn == 1:
        out = 1
        for i in lv:
            out *= i
        return out
    if tn == 2:
        return min(lv)
    if tn == 3:
        return max(lv)
    if tn == 5:
        return {True:1, False:0}[lv[0] > lv[1]]
    if tn == 6:
        return {True:1, False:0}[lv[0] < lv[1]]
    if tn == 7:
        return {True:1, False:0}[lv[0] == lv[1]]

with open('day16v1.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()][0]

bt = [] # bit transmission
for x in te:
    bt += hd[x] 

pot , vs = 0,0# pointer, version_sum
while sum(bt[pot:]) > 0:
    x = [a for a in rp(bt,pot)]
    pot = x[2]
    vs += x[4]

print("Part1:", vs)  
print("Part2:", evp(bt,0)[0])
