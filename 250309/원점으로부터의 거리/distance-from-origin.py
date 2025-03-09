import sys

class coordinate:
    def __init__(self,x,y,number):
        self.x = x
        self.y = y
        self.number = number

n = int(sys.stdin.readline())

l=[]
for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    l.append(coordinate(x,y,i+1))

l.sort(key = lambda x: abs(x.x-0)+abs(x.y-0))

for i in range(n):
    print(l[i].number)