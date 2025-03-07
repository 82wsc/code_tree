import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

a,b = list(a),list(b)

a.sort()
b.sort()

if a==b:
    print('Yes')
else:
    print('No')