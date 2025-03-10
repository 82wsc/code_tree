import sys

class student:
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight

n = int(sys.stdin.readline())


info = []
for _ in range(n):
    height,weight = map(int,sys.stdin.readline().split())
    info.append(student(height,weight))

info.sort(key = lambda x: (x.height, -x.weight))

for i in range(n):
    print(info[i].height,info[i].weight,i+1)