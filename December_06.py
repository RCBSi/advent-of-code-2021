with open('day06v1.txt', 'r') as file:
    t = [int(u) for u in [x.strip() for x in file.readlines()][0].split(",")]

ct0 = {i:0 for i in range(9)} 
for i in t: 
    ct0[i] += 1

gf = {i:1 for i in range(-1,1)}|{i:2 for i in range(1,8)} # seed a generalized Fibonacci sequence: 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4
for i in range(8,257):
    gf[i] = gf[i-9]+gf[i-7] # -9, -7 generalizes -1, -2 in the Fibonacci sequence.

print([(t,sum([gf[t-k]*ct0[k] for k in ct])) for t in [80,256]])

# Since -9 and -7 are odd, gf at odd values and gf at even values are not dependent on each other.
