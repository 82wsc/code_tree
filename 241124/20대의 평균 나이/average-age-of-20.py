import sys


n = int(sys.stdin.readline())
count=0
total=0

while n<30:
    total+=n
    count+=1
    n = int(sys.stdin.readline())
        
print(f"{total/count:.2f}")