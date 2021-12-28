import time
start = time.time()
with open('day24v1.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]

def i_to_b(x,b): # the base-be representation of x
    out = []
    while x > b:
        out.append(x % b)
        x = x//b
    out.append(x)
    out.reverse()
    return out

def solble(ad): # can the equation w == x + ad be solved?
    return int(ad) < 9

uin, hch = [9]*14, 1

while hch:
    w = x = y = z = j =  hch = 0
    i = -1
    con = ''
    stack = []
    for lin in te: 

        if lin == 'add x z':
            if stack:
                j = stack[-1]
            else:
                j = 0
        if lin[:6] == 'add x ' and lin != 'add x z':
            con = lin[6:]
        if lin == 'eql x w':
#            if x==w:
#                print(x,"=?=",w, "Holds!)
            if solble(con) and x != w:
#                print(w,"vs",x, ";", w,"depends on input",i,"while", x,"= z%26+",con, "depends on", stack, "and is",{0:"not", 1:"indeed"}[solble(con)],"solvable at",i0)
                if w < x and uin[j]-1 in range(1,10) and j not in lock and not hch:
                    uin[j] += -1
                    hch = 1
                elif x < w and i not in lock and uin[i]-1 in range(1,10) and not hch:
                    uin[i] += -1
                    hch = 1
        if lin == 'mul z y':
            if y == 26:
                dostack = 1
            if y == 1:
                dostack = 0
        if lin =='div z 26':
            stack = stack[:-1]
        if lin == 'add z y': # 'z' in lin: #
            if dostack:
                stack.append(i)

        upd = lin[4] 
        if lin[:3] == 'inp':
            i += 1
            es = upd+'=uin[i]'
            exec(es)
        oper = {'add':'+', 'div':'//','mul':'*', 'mod':'%', 'eql':'=='}

        if lin[:3] in oper:
            es = upd+' = int('+upd+oper[lin[:3]]+lin[6:]+')' 
            exec(es)                
    print(i_to_b(z,26), " ", stack, "".join([str(i3) for i3 in uin]))

print("Part 1", "".join([str(i3) for i3 in uin]))

uin = [1]*14
lock = {}
hch = 1
while hch:
    w = x = y = z = j =  hch = 0
    i = -1
    con = ''
    stack = []
    for lin in te: 

        if lin == 'add x z':
            if stack:
                j = stack[-1]
            else:
                j = 0
        if lin[:6] == 'add x ' and lin != 'add x z':
            con = lin[6:]
        if lin == 'eql x w':
#            if x==w:   # This reports which conditions hold.
#                print(x,"=?=",w, "Holds, locks",i,"relative to",j)

            if solble(con) and x != w:
#                print(w,"vs",x, ";", w,"depends on input",i,"while", x,"= z%26+",con, "depends on indices", stack, "with values", i_to_b(z,26), "and is",{0:"not", 1:"indeed"}[solble(con)],"solvable")
                if x < w and uin[j]+1 in range(1,10) and j not in lock and not hch:
                    uin[j] += 1
                    hch = 1
                elif w < x and j not in lock and uin[i]+1 in range(1,10) and not hch:
                    uin[i] += 1
                    hch = 1
        if lin == 'mul z y':
            if y == 26:
                dostack = 1
            if y == 1:
                dostack = 0
        if lin =='div z 26':
            stack = stack[:-1]
        if lin == 'add z y': 
            if dostack:
                stack.append(i)

        upd = lin[4]
        if lin[:3] == 'inp':
            i += 1
            es = upd+'=uin[i]'
            exec(es)
        oper = {'add':'+', 'div':'//','mul':'*', 'mod':'%', 'eql':'=='}
        if lin[:3] in oper:
            es = upd+' = int('+upd+oper[lin[:3]]+lin[6:]+')' 
            exec(es) 
    print(i_to_b(z,26), " ", stack, "".join([str(i3) for i3 in uin]))

print("p2", "".join([str(i3) for i3 in uin]))
