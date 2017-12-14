firewall = {0: {'layer':3,'scanner':[1,0,0],'move':1},
            1: {'layer':2,'scanner':[1,0],'move':1},
            4: {'layer':4,'scanner':[1,0,0,0],'move':1},
            6: {'layer':4,'scanner':[1,0,0,0],'move':1}}
packet = 0
epoch = 0
import sys
import copy
# firewall = { int(k):{'layer':int(v),'move':1,'scanner':[1]+[0]*(int(v)-1)} for k,v in [l.strip().split(':') for l in sys.stdin.readlines()]}

def print_firewall():
    print('================')
    for r in range(0,max(firewall.keys())+1):
        layer = firewall.get(r)
        if layer:
            print(r,firewall[r]['scanner'])

        else:
            print(r,'|')
    print('================')
def tick_scaner_move():
    for k,v in firewall.items():
        if v['scanner'][-1] == 1 and v['move']==1:
            v['move'] = -1
        if v['scanner'][0] == 1 and v['move']==-1:
            v['move'] = 1

        if v['move'] == 1:
           firewall[k]['scanner'] =  v['scanner'][-1:] + v['scanner'][:-1]
        if v['move'] == -1:
           firewall[k]['scanner'] =  v['scanner'][1:] + v['scanner'][0:1]


def tick():
    d = 0
    layer = firewall.get(packet,None)
    if layer and layer['scanner'][0]==1:
        d=packet*firewall[packet]['layer']

    tick_scaner_move()
    return d
print_firewall()

scanner_check=True
detection = []
"""
for epoch in range(0,max(firewall.keys())+1):

    detection.append(tick())
    packet +=1
print(sum(detection))
"""
savestate = copy.deepcopy(firewall)
delay= 0
detected = False
while True:
    packet = 0

    for r in range(0,delay):
        tick()
    print_firewall()
    for epoch in range(0,max(firewall.keys())+1):
        detected = tick()
        print(delay,detected)
        if detected:
            break
        packet+=1
    if not detected:
        print(delay)
        break
    delay+=1

    firewall = copy.deepcopy(savestate)







