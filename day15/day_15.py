def next(current,factor,constraint,divide=2147483647):
    while True:
        current = (current*factor) % divide
        if current % constraint == 0:
            return current

def gen(start,factor,constraint,size):
    while size >0:
        start = next(start,factor,constraint)
        yield start
        size -=1

A= 277
A_factor = 16807
A_constraint=4

B=349
B_factor = 48271
B_constraint = 8

def run(nb_iteration=5000000):
    return sum([1 for z in zip(gen(A,A_factor,A_constraint,5000000),gen(B,B_factor,B_constraint,5000000)) if format(z[0],'#032b')[-16:] == format(z[1],'#032b')[-16:] ])

print(run())