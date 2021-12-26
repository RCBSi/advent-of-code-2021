def readstate(text):
    return tuple([tuple([u for u in text[i0][1:12]]) for i0 in range(1,6)])

def readinitstate(filestr):
    with open(filestr, 'r') as file:
        te = [x.replace('\n','#').replace(' ','#') for x in file.readlines()]
    return readstate(te)

initstate = readinitstate('day23v1.txt')
initstring ='''#############
#...........#
###D#B#B#A###
  #D#C#B#A###
  #D#B#A#C###
  #C#C#D#A###
  ###########'''

okl = ('#','#','A','#','B','#','C','#','D','#','#')

p1state = (initstate[0],initstate[1],initstate[4],okl,okl)

def readtestcase(filestr):
    with open(filestr, 'r') as file:
        te = [x.replace('\n','#').replace(' ','#') for x in file.readlines()]
    return [readstate(te[i:i+7]) for i in range(0,len(te),8)]

#testcase = readtestcase('day23v3.txt') if you like, this was a nice example. 
# OTOH, lifting D to (0,3) #AA.D.....AD##AA.D.....AD# violates the heuristic:
# "always flow to the destination whenever possible, as a priority over any other move."
# That D which was lifted; its path to the destination was clear, so why stop early.

def isitsolved(stt): # state tuple; is it solved? 
    return stt == readstate('''#############
#...........#
###A#B#C#D###
###A#B#C#D###
###A#B#C#D###
###A#B#C#D###
#############'''.split('\n'))

def destination(stt,i,j): # is the token in i,j in its final destination square? If so, don't touch it.
    while i < 5:
        if stt[i][j] != {2:'A',4:'B',6:'C',8:'D'}[j]:
            return 0
        i+= 1
    return 1

def ready_to_go(stt,i,j): # is the token in i,j ready to go? 
    if i == 0:
        return 0
    if stt[i][j] == '.':
        return 0
    if stt[i-1][j] != '.':
        return 0
    if destination(stt,i,j):
        return 0
    return 1
    
def lift(stt): #stt = state tuple; Which tokens can be lifted to the "hallway"
    sta = [(i,j) for i in range(1,5) for j in range(2,9,2) if ready_to_go(stt,i,j)]
    accli = [((i,j),(0,j-1)) for (i,j) in sta if stt[0][j-1] not in 'ABCD']
    lpt = 0 # left pointer
    accri = [((i,j),(0,j+1)) for (i,j) in sta if stt[0][j+1] not in 'ABCD']
    rpt = 0
    while lpt < len(accli):
        ((i,j),(k,l)) = accli[lpt]
        next_candi = ((i,j),(k,l-2+(l<2)))
        if l>0 and stt[0][l-2+(l<2)] == '.':
            accli.append(next_candi)
        lpt += 1
    while rpt < len(accri):
        ((i,j),(k,l)) = accri[rpt]
        next_candi = ((i,j),(k,l+2-(l>8)))
        if l<10 and stt[0][l+2-(l>8)] == '.':
            accri.append(next_candi)
        rpt += 1
    return accli + accri

def validflowto(stt,i,j): # Is location i,j ready as a destination? 
    if stt[i][j] != '.':
        return 0 
    if j not in range(2,9,2):
        return 0
    if i == 4:
        return 1
    if i == 0:
        return 0
    if i == 3 and stt[i+1][j] == {2:'A',4:'B',6:'C',8:'D'}[j]:
        return 1
    if i == 2 and stt[i+1][j] == {2:'A',4:'B',6:'C',8:'D'}[j] and stt[i+2][j] == {2:'A',4:'B',6:'C',8:'D'}[j]:
        return 1
    if i == 1 and stt[i+1][j] == {2:'A',4:'B',6:'C',8:'D'}[j] and stt[i+2][j] == {2:'A',4:'B',6:'C',8:'D'}[j] and stt[i+3][j] == {2:'A',4:'B',6:'C',8:'D'}[j]:
        return 1        
    return 0

def findflowright(stt,i,j): # Destinations attract someone from the hall on the left..
    r = j
    while stt[0][r] == '.' and r < 10:
        r+=1
    if stt[0][r]== {2:'A',4:'B',6:'C',8:'D'}[j]:
        return ((i,j),(0,r))

def findflowleft(stt,i,j): # Destinations attract someone from the hall on the right..
    r = j
    while stt[0][r] == '.' and r > 0:
        r-=1
    if stt[0][r]== {2:'A',4:'B',6:'C',8:'D'}[j]:
        return ((i,j),(0,r))

def flowlr(stt): # All flow from the hallway to the rooms.
    end = [(i,j) for i in range(1,5) for j in range(2,9,2) if validflowto(stt,i,j)]
    ful = [x for x in [findflowleft(stt,i,j) for (i,j) in end] if x]
    fur = [x for x in [findflowright(stt,i,j) for (i,j) in end] if x]
    return [(b,a) for (a,b) in ful+fur]

def clear(stt,j,l): #Is the hallway clear between j and l. 
    if j==l:
        return 0
    j,l = min(j,l), max(j,l)
    return len(stt[0][j:l]) == stt[0][j:l].count('.')

def flowrr(stt): # All flow from room to room.
    sta = [(i,j) for i in range(1,5) for j in range(2,9,2) if stt[i][j] in 'ABCD' and (stt[i-1][j] not in 'ABCD')]
    end = [(i,j) for i in range(1,5) for j in range(2,9,2) if validflowto(stt,i,j)]
    return [((i,j),(k,l)) for (i,j) in sta for (k,l) in end 
    if stt[i][j]== {2:'A',4:'B',6:'C',8:'D'}[l] and clear(stt,j,l)]

def move(stt,i,j,k,l,m,n): # Update a tuple / create a new state tuple.
    if m==k and n==l:
        return stt[i][j]
    elif m==i and n==j:
        return '.'
    else: 
        return stt[m][n]

def mov(stt, mo): #execute the move
    ((i,j),(k,l)) = mo
    return tuple([
        tuple([
            move(stt,i,j,k,l,m,n) for n in range(len(stt[0]))
            ]) for m in range(len(stt)) 
        ])

def find_min_solution(from_state): # This searches all states. No attempt is made to eliminate permutations, sigh.
    sl = [from_state] #statelist, solution.
    #sl = [testcase[0]] # Good to go through this.
    parent = [0]
    movhere = [((0,0),(0,0))]
    pt = 0
    seen = {}
    while pt < len(sl):
        he = sl[pt]
        doflow = flowlr(he)+flowrr(he)
        if doflow:
            me = (doflow)[0]
            my = mov(he,me)
            if my not in seen:
                sl.append(my)
                parent.append(pt)
                movhere.append(me)
                seen[sl[pt]] = pt
        else:
            dorise = lift(he)
            for me in dorise: # lift 
                my = mov(he,me)
                if my not in seen:# my in testcase:
                    sl.append(my)
                    parent.append(pt)
                    movhere.append(me)
                    seen[sl[pt]] = pt
        pt+=1

    sol = [i for i in range(len(sl)) if isitsolved(sl[i])] # 146.
    score = {}
    for i in range(len(sol)):
        di = 0#{'A':0,'B':0,'C':0,'D':0}
        pt = sol[i]
        while pt > 0:
            ((i,j),(k,l)) = movhere[pt]
            sprite = sl[pt][k][l] 
            sm = {'A':1,'B':10,'C':100,'D':1000}[sprite]
            di += (i+k+abs(j-l)) * sm
            pt = parent[pt]
        if di <= 50182*2:
            score[di] = sol[i]
    if score:
       return min(score)        

print("day23 part 1:", find_min_solution(p1state))
print("day23 part 2:", find_min_solution(initstate))
