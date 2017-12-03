import sys
data=sys.stdin.read()
# Part 01
print(sum([int(r) for l,r in zip(data,data[1:]+data[0]) if l==r]))

# Part 02
print(sum([int(r) for l,r in zip(data[len(data)//2:],data[:len(data)//2]) if l==r])*2)