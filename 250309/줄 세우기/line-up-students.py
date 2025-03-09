import sys

class student:
    def __init__(self,height,weight,number):
        self.height = height
        self.weight = weight
        self.number = number

n = int(sys.stdin.readline())

l = []
for i in range(n):
    height,weight = map(int,sys.stdin.readline().split())
    l.append(student(height,weight,i+1))

l.sort(key = lambda x: (-x.height,-x.weight))

for i in range(n):
    print(l[i].height, l[i].weight,l[i].number )