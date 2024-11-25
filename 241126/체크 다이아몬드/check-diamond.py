import sys

n = int(sys.stdin.readline())

for i in range(1,n+1):
    print(' '*(n-i)+' '.join('*'*i))
for i in range(1,n+1):
    print(' '*i+' '.join('*'*(n-i)))