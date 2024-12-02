import sys

s = list(sys.stdin.readline().strip())

for i in range(len(s)):
    if s[i]=='e':
        s[i]=''
        break

print(*s,sep='')