import sys


l = []
for _ in range(3):
    l.append(len(sys.stdin.readline().strip()))

print(max(l)-min(l))



