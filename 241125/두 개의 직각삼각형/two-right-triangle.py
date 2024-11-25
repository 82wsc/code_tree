import sys

n = int(sys.stdin.readline())

for i in range(n):
    print('*'*(n-i)+' '*i*2+'*'*(n-i))