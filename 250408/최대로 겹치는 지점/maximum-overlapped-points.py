import sys

n = int(sys.stdin.readline())

l = [0] * 99

for i in range(n):
    s,e = map(int,sys.stdin.readline().split())
    for j in range(s,e+1):
        l[j]+=1
    
print(max(l))