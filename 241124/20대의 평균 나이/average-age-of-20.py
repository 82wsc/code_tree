import sys

l=[]
n = int(sys.stdin.readline())
while n<30:
    l.append(n)
    n = int(sys.stdin.readline())
        
print(f"{sum(l)/len(l):.2f}")