def up(x,y): # boolean "is this an increase"
    if y > x: 
        return 1
    else:
        return 0

def up_seq(t,k): # k = offset.
    return [up(t[i],t[i+k]) for i in range(len(t)-k)]

with open('day01v1.txt', 'r') as file:
    t = [int(x.strip()) for x in file.readlines()]

print("part1:",sum(up_seq(t,1)))
print("part2:",sum(up_seq(t,3)))
