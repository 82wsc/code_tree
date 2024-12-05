import sys

a,b = map(int,sys.stdin.readline().split())

A =list(map(int,sys.stdin.readline().split()))
B =list(map(int,sys.stdin.readline().split()))


def part_arr(x,y):
    for i in range(a-b+1):
        if A[i:i+b] == B:
            return 'Yes' 
    return 'No' 

print(part_arr(A,B))