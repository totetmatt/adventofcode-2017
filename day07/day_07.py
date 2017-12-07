import sys
data = [l.strip() for l in sys.stdin.readlines()]
nodes = {}
edges = {}
tree ={}
for d in data:
    l = d.split('->')
    source=l[0]
    nodes[source.split(' ')[0]]=int(source.split(' ')[1].replace('(','').replace(')',''))
    if len(l) > 1:
        targets = [w.strip() for w  in l[1].strip().split(',')]
        for e in targets:
            edges[e] =source.split(' ')[0]
        tree[source.split(' ')[0]] = targets
r = [ l for l in edges.keys()][0]

balance = {}

for k,v in edges.items():
    w = nodes[k]
    if k not in balance:
        balance[k] = w
    else:
        balance[k] += w

root = 'vmpywg'
wtree = {}
def traverse(node,layer=0):
    if layer not in wtree:
        wtree[layer] = {}
    w = nodes[node]
    if tree.get(node,None):
        w += sum([traverse(k,layer+1) for k in  tree.get(node,None) ])
    wtree[layer][node] = w
    print(node,nodes[node],w)
    return w
traverse(root)
print([(l,v) for l,v in wtree[1].items() if  l in tree[root]])
print([(l,v) for l,v in wtree[2].items() if  l in tree['ndjsvna']])
print([(l,v) for l,v in wtree[3].items() if  l in tree['orflty']])
print([(l,v) for l,v in wtree[4].items() if  l in tree['ncrxh']])
print(nodes['ncrxh'])
print(tree['ndjsvna'])
"""
while True:
    print(r,nodes[r])
    c = edges.get(r,None)
    if not c :

        break
    r = c
"""