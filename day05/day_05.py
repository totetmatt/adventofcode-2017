import sys

DATA = [int(l) for l in sys.stdin.readlines()]
print(DATA)
TEST = [0,3,0,1,-3]

idx = 0
cpt = 0
while idx <= len(DATA):

    jump =  DATA[idx]
    DATA[idx] +=1
    idx = idx + jump
    cpt+=1
    if idx >= len(DATA):
        break
print("== %s =="%cpt)