import sys

n = int(sys.stdin.readline())
cnt=9
for i in range(n):
    for j in range(n):
        if cnt-j<1:
            cnt=10    
        print(cnt-j,end='')
    print()
    cnt-=n
    