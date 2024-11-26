import sys

n = int(sys.stdin.readline())

for i in range(n,0,-1):
    for j in range(1,i+1):
        if j==i:
            print(f"{n-i+1} * {j} = {(n-i+1)*j}",end=' ')
        else:
            print(f"{n-i+1} * {j} = {(n-i+1)*j}",end=' / ')
    print()