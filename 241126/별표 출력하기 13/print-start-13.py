import sys

n = int(sys.stdin.readline())

for i in range(1,n+1):
    if i%2==1:
        print(' '.join('*'*int(i*(-0.5)+3.5)))
    else:
        print(' '.join('*'*int(i//2)))    
for i in range(n,0,-1):
    if i%2==1:
        print(' '.join('*'*int(i*(-0.5)+3.5)))
    else:
        print(' '.join('*'*int(i//2)))     