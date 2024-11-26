import sys

a,b = map(int,sys.stdin.readline().split())

for i in range(1,5):
    for j in range(b,a-1,-1):
        if j==a:
            print(f"{j} * {2*i} = {j*2*i}",end=' ')
        else:
            print(f"{j} * {2*i} = {j*2*i}",end=' / ')    
    print()