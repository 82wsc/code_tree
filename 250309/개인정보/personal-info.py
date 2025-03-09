import sys

class info:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
n=5
l = []
for _ in range(n):
    name,height,weight = sys.stdin.readline().split()
    height = int(height)
    weight = float(weight)
    l.append(info(name,height,weight))

l.sort(key = lambda x : x.name)

print('name')
for i in range(n):
    print(l[i].name,l[i].height,l[i].weight)

l.sort(key = lambda x : -x.height)

print('')
print('height')
for i in range(n):
    print(l[i].name,l[i].height,l[i].weight)
