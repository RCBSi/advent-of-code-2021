import time
import numpy

def allowed(p,x):
# part 1: return ((x not in sm) or (e[1] not in p))
    if x == 'start':
        return False
    if ((x not in sm) or x not in p):
        return True
    if p.count(x) > 1:
        return False
    if max([p.count(c) for c in sm]) < 2: #or for part 1 remove this.
        return True #or make this false (for part 1).

def s1(p): #take one more step.
    output_finished_paths = []
    output_unfinished_paths = []
    lo = p[-1]
    for e in ed:
        if e[0] == lo:
            if e[1] == 'end':
                output_finished_paths.append(p+[e[1]])
            elif allowed(p,e[1]):
                output_unfinished_paths.append(p+[e[1]])
    return [output_unfinished_paths, output_finished_paths]

with open('day12v1.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]

ed = []
for st in te:
    [a,b] = st.split('-')
    ed.append([a,b])
    ed.append([b,a]) 

pa = []
for [a,b] in ed:
    if a == 'start':
        pa.append([a,b])

ca = numpy.unique(ed)
sm = ca[4:] # set this by hand to include all lower-case cave names; "small" caves.

start = time.time()
ep = [] # paths to the end
while pa: # depth-first search is what they used. 
    p = pa.pop()
    [new_ongoing, new_ended] = s1(p)
    if new_ongoing:
        pa.extend(new_ongoing)
    if new_ended:
        ep.extend(new_ended)

print(time.time() - start, len(ep))
# nontrivial runtime 9 seconds.
