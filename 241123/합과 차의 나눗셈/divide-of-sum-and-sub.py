import sys

a,b = map(int,sys.stdin.readline().split())
s=a+b
m=a-b
print(f"{s/m:.2f}")