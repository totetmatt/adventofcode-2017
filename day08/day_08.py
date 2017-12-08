import re
import collections
import sys
reg = collections.Counter()
max_reg = 0
TEST = ['b inc 5 if a > 1',
        'a inc 1 if b < 5',
        'c dec -10 if a >= 1',
        'c inc -20 if c == 10'
        ]

def use_reg(str):
    return re.sub(r"([a-z]+)",r"reg['\1']",str)

def parse(str):
    return str.replace('inc','+').replace('dec','-').split('if')


TEST = [l.strip() for l in sys.stdin.readlines()]
for l in TEST:
    instruction,condition= parse(l)
    print(instruction)
    if eval(use_reg(condition)):
        reg[instruction.split(' ')[0]] = eval(use_reg(instruction))
    max_reg = max(max_reg,reg.most_common()[0][1])
print(max_reg)
print(reg.most_common())