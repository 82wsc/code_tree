import sys

def even(arr):
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[i]=arr[i]//2

    print(*arr,end='')

n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))

even(l)
