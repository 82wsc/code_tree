import sys

a,b,c = map(int,sys.stdin.readline().split())

med = 0

if a>b>c:
    med = b
elif a>c>b:
    med = c
elif b>a>c:
    med = a
elif b>c>a:
    med = c
elif c>a>b:
    med = a
elif c>b>a:
    med = b
print(med)
