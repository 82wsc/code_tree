import sys

s = sys.stdin.readline()
l=[]
for i in range(len(s)):
    if i%2==1:
        l.append(s[i])
l=l[::-1]
print(*l,sep='')