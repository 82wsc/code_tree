import sys

class info:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(sys.stdin.readline())

l = []
for _ in range(n):
    name, height, weight = sys.stdin.readline().split()
    height, weight = int(height), int(weight)
    l.append(info(name,height,weight))

l.sort(key = lambda x: (x.height, -x.weight))

for i in range(n):
    print(l[i].name, l[i].height, l[i].weight)