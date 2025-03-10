import sys

class student:
    def __init__(self,height,weight,idx):
        self.height = height
        self.weight = weight
        self.idx = idx

n = int(sys.stdin.readline())


info = []
for i in range(n):
    height,weight = map(int,sys.stdin.readline().split())
    info.append(student(height,weight,i+1))

info.sort(key = lambda x: (x.height, -x.weight))

for i in range(n):
    print(info[i].height,info[i].weight,info[i].idx)