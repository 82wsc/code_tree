import sys
a,b,c = map(int,sys.stdin.readline().split())

s=a+b+c
aver = int(s/3)

print(s)
print(aver)
print(s-aver)