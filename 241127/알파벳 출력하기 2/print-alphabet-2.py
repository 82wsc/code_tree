import sys

n = int(sys.stdin.readline())

# A:65
cnt=65
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print(chr(cnt),end=" ")
        cnt+=1
    print()

