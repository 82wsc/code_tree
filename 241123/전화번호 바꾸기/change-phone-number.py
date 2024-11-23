import sys

s = sys.stdin.readline()

s = list(s)

s[4:8], s[9:13] =s[9:13],s[4:8]

print(*s,sep='')