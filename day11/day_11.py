import functools
import sys
maper = {'n':(0,1,0), 'ne':(1,0,0),'se':(1,-1,0), 'nw':(-1,1,0),'sw':(-1,0,0),'s':(0,-1,0)}
def hex_distance(a, b): return (abs(a[0] - b[0]) + abs(a[0] + a[1] - b[0] - b[1]) + abs(a[1] - b[1])) / 2
data = [maper[k] for k in sys.stdin.read().strip().split(',')]
final =functools.reduce(lambda x,y:  (x[0]+y[0],x[1]+y[1],max(hex_distance((0,0),(x[0]+y[0],x[1]+y[1])),x[2])),data)
print(final,hex_distance((0,0),final))