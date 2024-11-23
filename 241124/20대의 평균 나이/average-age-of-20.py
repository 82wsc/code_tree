import sys

l=[]
while True:
    n = int(sys.stdin.readline())
    if n>=30:
        break
    else:
        l.append(n)
        
print(f"{sum(l)/len(l):.2f}")