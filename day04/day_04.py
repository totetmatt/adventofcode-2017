import sys
import collections
data = sys.stdin.readlines()
c = sum( [1for l in data if collections.Counter(l.strip().split(' ')).most_common(1)[0][1]==1])
print(c)

c = sum( [1for l in data if collections.Counter([ "".join(sorted(k)) for k in l.strip().split(' ')]).most_common(1)[0][1]==1])
print(c)