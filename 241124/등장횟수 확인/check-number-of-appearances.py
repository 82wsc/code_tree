import sys

idx=0
for _ in range(5):
    n = int(sys.stdin.readline())
    if n%2==0:
        idx+=1
print(idx)