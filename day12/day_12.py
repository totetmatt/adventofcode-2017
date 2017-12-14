import sys
for r in sys.stdin.readlines():
    print(r.strip().replace('<->',',').replace(' ',''))