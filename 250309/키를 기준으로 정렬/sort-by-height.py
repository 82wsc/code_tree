import sys

class height:
    def __init__(self,name,h,w):
        self.name = name
        self.h = h
        self.w = w

n = int(sys.stdin.readline())

l=[]
for _ in range(n):
    name, h, w = sys.stdin.readline().split()
    h,w = int(h), int(w)
    l.append(height(name,h,w))

l.sort(key=lambda x: x.h)

for i in range(n):
    print(l[i].name,l[i].h,l[i].w)