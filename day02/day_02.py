import sys
import itertools

data = [[int(k) for k in l.strip().split('\t')] for l in sys.stdin.readlines() ]
# Part 01
print(sum([max(p)-min(p) for p in data ]))
# Part 02
print(sum([a//b for sublist in data for a,b in itertools.permutations(sublist,2) if a>b and a%b==0]))

