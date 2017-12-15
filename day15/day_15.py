def next(current,factor,constraint,divide=2147483647):
    while True:
        current = (current*factor) % divide
        if current % constraint == 0:
            return current



"""
Generator A starts with 277
Generator B starts with 349
"""
A= 277
A_factor = 16807
A_constraint=4

B=349
B_factor = 48271
B_constraint = 8
cpt = 0


for r in range(0,5000000):
    # print(format(A,'#032b')[-16:],A)
    # print(format(B,'#032b')[-16:],B)
    if format(A,'#032b')[-16:] == format(B,'#032b')[-16:]:
        cpt +=1
    # print('----')
    A = next(A,A_factor,A_constraint)
    B = next(B,B_factor,B_constraint)

print(cpt)