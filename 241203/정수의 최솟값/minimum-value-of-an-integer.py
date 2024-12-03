import sys

a,b,c = map(int,sys.stdin.readline().split())

def find_min(a,b,c):
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    return min(l)
    
print(find_min(a,b,c))
