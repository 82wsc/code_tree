import sys

n = int(sys.stdin.readline())
idx=0
while n>=1:
    idx+=1
    n=n//idx
    
print(idx)