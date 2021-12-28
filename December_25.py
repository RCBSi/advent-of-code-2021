import time
start = time.time()
with open('day25v1.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]

M = [list(u) for u in te]
moved = 1
clock = 0

while moved:
    rm = [[0 for j in range(len(M[0]))] for i in range(len(M))] #ready to move

    for i in range(len(M)):
        for j in range(len(M[0])-1):
            if M[i][j] == '>' and M[i][j+1] == '.':
                rm[i][j] = 1
    j = len(M[0])-1
    for i in range(len(M)):
        if M[i][j] == '>' and M[i][0] == '.':
            rm[i][j] = 1  

    move_right = sum([sum(rm[i]) for i in range(len(M))])

    for i in range(len(M)):
        for j in range(len(M[0])-1):
            if rm[i][j] == 1:
                M[i][j] = '.' 
                M[i][j+1] = '>'                
    j = len(M[0])-1
    for i in range(len(M)):
        if rm[i][j] == 1:
            M[i][j] = '.' 
            M[i][0] = '>' 

    rm = [[0 for j in range(len(M[0]))] for i in range(len(M))] #ready to move

    for i in range(len(M)-1):
        for j in range(len(M[0])):
            if M[i][j] == 'v' and M[i+1][j] == '.':
                rm[i][j] = 1
    i = len(M)-1
    for j in range(len(M[0])):
        if M[i][j] == 'v' and M[0][j] == '.':
            rm[i][j] = 1  

#    [print(''.join([str(x) for x in ro]))  for ro in rm]

    moved = move_right + sum([sum(rm[i]) for i in range(len(M)-1)])
    if moved:
        clock += 1
    if clock%29 ==1:
        print(clock, move_right, moved, len(M), time.time()-start)

    for i in range(len(M)-1):
        for j in range(len(M[0])):
            if rm[i][j] == 1:
                M[i][j] = '.' 
                M[i+1][j] = 'v'
    i = len(M)-1
    for j in range(len(M[0])):
        if rm[i][j] == 1:
            M[i][j] = '.' 
            M[0][j] = 'v'         

#[print(''.join(ro))  for ro in M]

print("Part1:", clock+1)
print("Part2:", 1)

