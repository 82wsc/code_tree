import sys

a,b = map(int,sys.stdin.readline().split())

x=1
for i in range(1,b):
    if i%a==0:
        x*=i
print(x)