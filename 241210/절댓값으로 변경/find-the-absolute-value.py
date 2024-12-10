import sys

def num_abs(arr):
    for i in range(len(arr)):
        arr[i]=abs(arr[i])
    
    print(*arr,end='')

n = int(sys.stdin.readline())

l=list(map(int,sys.stdin.readline().split()))

num_abs(l)