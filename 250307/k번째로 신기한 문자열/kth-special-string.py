import sys

n,k,s = sys.stdin.readline().split()
n,k= int(n),int(k)

a=[]
for i in range(n):
    x= sys.stdin.readline().strip()
    if x[:len(s)]==s:
        a.append(x)

a.sort()

print(a[k-1])