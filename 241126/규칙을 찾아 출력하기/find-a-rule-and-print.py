import sys

n = int(sys.stdin.readline())

print(' '.join('*'*n))
for i in range(1,n):
  print(' '.join('*'*i+' '*(n-i-1)+'*'))