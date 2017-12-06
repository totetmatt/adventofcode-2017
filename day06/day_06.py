import sys

states = {}
cpt=0

TEST = [0,2,7,0]

TEST =[int(v) for v in sys.stdin.read().split('\t')]
size = len(TEST)
print(TEST)
# print(TEST.index(max(TEST)))
states[str(TEST)] = cpt
while True:

    a = max(TEST)
    idx = TEST.index(a)

    TEST[idx]=0
    curr_idx = (idx +1)  % size
    for _ in range(0,a):
        TEST[curr_idx] += 1
        curr_idx = (curr_idx + 1) % size

    cpt +=1
    if str(TEST) in states :
        break

    states[str(TEST)] = cpt


print(cpt,cpt - states[str(TEST)])


