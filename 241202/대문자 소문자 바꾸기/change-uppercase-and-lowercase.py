import sys

s = list(sys.stdin.readline().strip())

for i in range(len(s)):
    if s[i].isupper():
        s[i]=s[i].lower()
    else:
        s[i]=s[i].upper()
print(*s,sep='')