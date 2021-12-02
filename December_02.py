with open('day02v1.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]

diton = {'forward':1, 'down':1j, 'up':-1j} #direction to number

pos = 0
for ins in t:
    [dir, dis] = ins.split(" ")
    pos += diton[dir]*int(dis)

print("Part1:", round(pos.real * pos.imag))

(pos, aim) = (0,1)
for ins in t:
    [dir, dis] = ins.split(" ")
    if dir == 'forward':
        pos += aim*int(dis)
    if dir in ['up','down']:
        aim += diton[dir]*int(dis)

print("Part2:", round(pos.real * pos.imag))
