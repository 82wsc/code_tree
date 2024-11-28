import sys


a = list(map(int,sys.stdin.readline().split()))

for i in range(2,10):
    a.append(a[i-1]+a[i-2]*2)

print(*a,sep=' ')

# A3 = A2 +2A1