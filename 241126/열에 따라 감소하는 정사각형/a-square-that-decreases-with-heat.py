import sys

n = int(sys.stdin.readline())

for i in range(n):
    for j in range(n):
        print(n-j,end=' ')
    print()