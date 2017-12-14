input = 'flqrgnkx'
convert = { s:"{0:4b}".format(int(s, 16)) for s in "abcdef0123456789"}
data = ['%s-%s'%(input,r) for r in range(0,128)]

print(data)

print(convert)
