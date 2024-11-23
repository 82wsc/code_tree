import sys

a,b,c = map(int,sys.stdin.readline().split())

if c>b>a:
    print(1)
else:
    print(0)