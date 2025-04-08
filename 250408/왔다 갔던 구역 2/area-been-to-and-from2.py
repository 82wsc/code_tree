import sys

n = int(sys.stdin.readline())

segments = [
    tuple(input().split())
    for _ in range(n)
]

l = [0]*202
c = 100

for a,b in segments:
    a = int(a)
    if b == 'R':
        for i in range(c,c+a):
            l[i] +=1
        
        c += a
    
    if b == 'L':
        for i in range(c-a,c):
            l[i] +=1
        
        c -= a

leng = 0

for i in range(len(l)):
    if l[i]>=2:
        leng += 1

print(leng)