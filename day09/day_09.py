test = {
"{}": 1,
"{{{}}}":6,
"{{},{}}": 5,
"{{{},{},{{}}}}":16,
"{<a>,<a>,<a>,<a>}":1,
"{{<ab>},{<ab>},{<ab>},{<ab>}}": 9,
"{{<!!>},{<!!>},{<!!>},{<!!>}}":9,
"{{<a!>},{<a!>},{<a!>},{<ab>}}":3}

import re
import sys

data = sys.stdin.read().strip()
def remove_ignore_garage(string) : return re.sub('!.', '',string)

def run_recursion_not_working_for_large_input_call_dicaprio(data,depth=1,acc=0,garbage=False):
    if not data or len(data)==1:
        return acc
    head,*tail =data
    if garbage:
        if head == ">":
            return run_recursion_not_working_for_large_input_call_dicaprio(tail,depth,acc)
        else :
            return run_recursion_not_working_for_large_input_call_dicaprio(tail,depth,acc,True)
    elif head=='{' :
        return run_recursion_not_working_for_large_input_call_dicaprio(tail,depth+1,acc+depth)
    elif head=='}' :
        return run_recursion_not_working_for_large_input_call_dicaprio(tail,depth-1,acc)
    elif head == '<':
        return run_recursion_not_working_for_large_input_call_dicaprio(tail,depth,acc,True)
    else:
        return run_recursion_not_working_for_large_input_call_dicaprio(tail,depth,acc)

def run(data,depth=0,acc=0,garbage=False,garbage_count=0):
    head,*tail =data
    while tail:
        if garbage:
            if head == ">":
                garbage = False
            else :
                garbage_count +=1
        elif head=='{' :
            depth+=1
            acc+=depth
        elif head=='}' :
            depth-=1
        elif head == '<':
            garbage = True
        head,*tail =tail
    return acc,garbage_count

for i,v in test.items():
    print(i,remove_ignore_garage(i),v,run_recursion_not_working_for_large_input_call_dicaprio(remove_ignore_garage(i)))
print(run(remove_ignore_garage(data)))

