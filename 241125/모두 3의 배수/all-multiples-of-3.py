import sys

r=True
for _ in range(5):
    n = int(sys.stdin.readline())
    if n%3!=0:
        r=False
        break
        
if r==True:
    print(1)
else:
    print(0)
