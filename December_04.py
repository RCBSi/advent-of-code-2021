def tr(board): #transpose
    return [[board[i][j] for i in range(5)] for j in range(5)] 

def sco(b, tim, t): #score the board at the time t
    return sum([int(x)*(tim[x] > t) for r in b for x in r])

def wt(a,bt): # win-time for a row, given ball-time.
    return max(bt[x] for x in a)

with open('day04v2.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]

boards = [[s.split() for s in t[x:x+5]] for x in range(2,len(t),6)]
bs = [sum([int(x) for r in b for x in r]) for b in boards]

tb = t[0].split(",") # time=index, ball-value.
bat = {tb[k]:k for k in range(len(tb))} # ball : time.
tib = {min([wt(a,bat) for a in boards[i] + tr(boards[i])]):i for i in range(len(boards))} #time:board.

print("Part1:", int(tb[min(tib)]) * sco(boards[tib[min(tib)]],bat,min(tib)))
print("Part2:", int(tb[max(tib)]) * sco(boards[tib[max(tib)]],bat,max(tib)))
