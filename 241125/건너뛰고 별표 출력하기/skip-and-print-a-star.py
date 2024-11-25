import sys

n = int(sys.stdin.readline())

for i in range(1,n):
    print('*'*i)
    print()
for i in range(n):
    print('*'*(n-i))
    print()