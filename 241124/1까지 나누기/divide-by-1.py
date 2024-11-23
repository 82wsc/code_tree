import sys

n = int(sys.stdin.readline())
idx=1
while n>0:
    n=n//idx
    idx+=1

print(idx-1)