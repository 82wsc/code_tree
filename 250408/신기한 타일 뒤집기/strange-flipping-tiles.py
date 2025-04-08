import sys

n = int(sys.stdin.readline())

segments = [
    tuple(sys.stdin.readline().split())
    for _ in range(n)
]

l = [0] * 201
c = 100

for a,b in segments:
    a = int(a)

    if b=='R':
        for i in range(c+1,c+a):
            l[i]='B'
        c += a

    if b=='L':
        for i in range(c,c-a,-1):
            l[i]='W'
        c -= a

b,w = 0,0

for i in range(len(l)):
    if l[i]=='B':
        b+=1
    if l[i]=='W':
        w+=1

print(w,b)