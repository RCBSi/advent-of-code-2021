import time
import numpy

def allowed(p,x):
# part 1: return ((x not in sm) or (e[1] not in p))
    if x == 'start':
        return False
    if (x.isupper() or x not in p):
        return True
    if p.count(x) > 1:
        return False
    if max([p.count(c) for c in sm]) < 2: #or for part 1 remove this.
        return True #or make this false (for part 1).

def s1(p): #take one more step.
    output_finished_paths = []
    output_unfinished_paths = []
    lo = p[-1]
    for e1 in de[lo]:
        if e1 == 'end':
            output_finished_paths.append(p+[e1])
        elif allowed(p,e1):
            output_unfinished_paths.append(p+[e1])
    return [output_unfinished_paths, output_finished_paths]

with open('day12v1.txt', 'r') as file:
    te = [x.strip() for x in file.readlines()]

ed = []
for st in te:
    [a,b] = st.split('-')
    ed.append([a,b])
    ed.append([b,a]) 

de = {x:[] for (x,y) in ed if x != 'end'} # degree
for (x,y) in ed:
    if x != 'end':
        if y not in de[x] and y != 'start':
            de[x].append(y)

pa = []
for b in de['start']:
        pa.append(['start',b])

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

print(time.time() - start, len(ep), "while pa, ep.extend(new_ended)")
start = time.time()

def cl(lc,se,se2): # count legitimate paths, indexing them by recursion, without listing paths.
    if lc == 'end':
        return 1
    clfrn = 0 #count legitimate paths from this recursion node.
    for c2 in de[lc]:
        if c2 not in se and c2.islower():
            clfrn += cl(c2,se+[c2],se2)
        elif c2 not in se and c2.isupper():
            clfrn += cl(c2,se,se2)
        elif not se2:
            clfrn += cl(c2,se,[c2])
    return clfrn
print(time.time() - start, cl('start',[],[]), "count legitimate paths with recursion indexing them")
#
# 4.104459762573242 9xxx2 while pa, ep.extend(new_ended)
# 0.00019884109497070312 9xxx2 count legitimate paths with recursion indexing them, building neither paths nor the list of paths.
# 
