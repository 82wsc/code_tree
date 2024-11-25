import sys

a,b = map(int,sys.stdin.readline().split())

if a>0:
    for _ in range(b):
        print(a,end='')
else:
    print(0)