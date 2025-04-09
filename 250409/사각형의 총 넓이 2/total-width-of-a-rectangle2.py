import sys

n = int(sys.stdin.readline())

l=[[0 for i in range(201)] for j in range(201)]

segments = [
    tuple(map(int,sys.stdin.readline().split()))
    for _ in range(n)
]

for x1,y1,x2,y2 in segments:
    for i in range(x1,x2):
        for j in range(y1,y2):
            l[i][j]+=1

area = 0

for i in range(201):
    for j in range(201):
        if l[i][j] >=1:
            area +=1

print(area)
    
