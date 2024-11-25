import sys

a,b = map(int,sys.stdin.readline().split())

if a < b:
    pass
else:
    current = a
    while current >= b:  
        if current % 2 == 0:
            print(current, end=" ")
        current -=1