def tr(board): #transpose
    return [[board[i][j] for i in range(5)] for j in range(5)] 

def sco(b, tim, t): #score the board at the time t
    return sum([int(x)*(tim[x] > t) for r in b for x in r])

with open('day04v2.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]

i=0
rando = t[i].split(",")
i+=2
boards = []
while i < len(t):
    boards.append([s.split() for s in t[i:i+5]])
    i += 6

tim = {}
for i in range(len(rando)):
    tim[rando[i]] = i

bs = []#board sum
for b in boards:
    bs.append(sum([int(x) for r in b for x in r]))
    

(gt, sc) = (len(rando),0) #game time, score delta
for i in range(len(boards)):
    for wl in boards[i] + tr(boards[i]):
        if max([tim[x] for x in wl]) < gt:
            gt = max([tim[x] for x in wl])
            sc = sco(boards[i],tim,gt)
#            sc = bs[i] - sum([int(x) for x in wl])
            print("t=",gt,"wl=", wl, "score -=",sc)

print("Part1:", int(rando[gt])*sc)

(gt,sc, lb) = (0,0,0) #game time, score delta, loserboard
for i in range(len(boards)):
    bt = len(rando) # board time
    for wl in boards[i] + tr(boards[i]):
        if max([tim[x] for x in wl]) < bt:
            bt = max([tim[x] for x in wl])
            sc = sco(boards[i],tim,gt)
#            sc = bs[i] - sum([int(x) for x in wl])
#            print("t=",gt,"wl=", wl, "score -=",sc)
#    print("board #",i,"won in time",bt)
    if bt > gt:
        lb = i
        gt = bt
        sc = sco(boards[i],tim,gt)
        
print("Part2:", int(rando[gt])*sco(boards[lb],tim,gt))

