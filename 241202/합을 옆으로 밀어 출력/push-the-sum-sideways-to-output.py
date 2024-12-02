import sys

n = int(sys.stdin.readline().strip())

s=0
for _ in range(n):
    s += int(sys.stdin.readline().strip())

s = list(str(s))
temp = s[0]
s=s[1:]
s.append(temp) 
print(*s,sep='')