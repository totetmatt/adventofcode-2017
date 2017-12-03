

class NavMap:

    def __init__(self):
        self.current_direction = 'r'
        self.current_position=(0,1)
        self.data = {(0,0):1,(0,1):2}
    def addSquare(self):
        v = self.data[self.current_position]
        dir,x,y=self._nextPosition(self.current_position,self.current_direction)

        self.current_position=(x,y)
        self.current_direction=dir
        self.data[self.current_position] = v+1
        return v+1,dir,x,y
    def _nextPosition(self,pos,dir):
        x,y = pos
        if dir == 'r':
            if self.data.get((x+1,y),None):
                return (dir,x,y+1)
            else:

                return ('u',x+1,y)
        if dir == 'l':
            if self.data.get((x-1,y),None):
                return (dir,x,y-1)
            else:
                return ('d',x-1,y)
        if dir == 'u':
            if self.data.get((x,y-1),None):
                return (dir,x+1,y)
            else:
                return ('l',x,y-1)
        if dir == 'd':
            if self.data.get((x,y+1),None):
                return (dir,x-1,y)
            else:
                return ('r',x,y+1)

m = NavMap()
v = 0
dir = None
x = None
y = None
input = 368078
while v < input :
    v,dir,x,y = m.addSquare()
print(v,dir,x,y)

print(sum([abs(x),abs(y)]))

