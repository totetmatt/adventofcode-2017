import sys
import collections
states = {}
cpt=0

DATA = [0, 2, 7, 0]
DATA =[int(v) for v in sys.stdin.read().split('\t')]
while True:
    print(DATA)
    a = max(DATA)
    idx = DATA.index(a)
    size = len(DATA)
    distrib =  collections.Counter((idx + r)%size for r in range(1,a+1))
    DATA[idx] = 0
    DATA = [distrib.get(i, 0) + v for i, v in enumerate(DATA)]
    cpt+=1
    if str(DATA) in states:
        break
    states[str(DATA)] = cpt

print(cpt, cpt - states[str(DATA)])
