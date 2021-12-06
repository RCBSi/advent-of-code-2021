def tr(board): #transpose
    return [[board[i][j] for i in range(5)] for j in range(5)] 

def sco(b, tim, t): #score the board at the time t
    return sum([int(x)*(tim[x] > t) for r in b for x in r])

def wt(a,bt): # win-time for a row, given ball-time.
    return max(bt[x] for x in a)

with open('day04v2.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]

boards = [[s.split() for s in t[x:x+5]] for x in range(2,len(t),6)]

tiba = t[0].split(",") # time=index, ball-value.
bati = {tiba[k]:k for k in range(len(tiba))} # ball : time.
tibo = {min([wt(a,bati) for a in boards[i] + tr(boards[i])]):i for i in range(len(boards))} #time:board.

print("Part1:", int(tiba[min(tibo)]) * sco(boards[tibo[min(tibo)]],bati,min(tibo)))
print("Part2:", int(tiba[max(tibo)]) * sco(boards[tibo[max(tibo)]],bati,max(tibo)))
