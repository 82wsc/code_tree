import sys

a,b = map(int,sys.stdin.readline().split())

def prime_number(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def even_number(n):
    if ((n//10)+(n%10))%2==0:
        return True

cnt=0
for i in range(a,b+1):
    if prime_number(i) and even_number(i):
        cnt+=1

print(cnt)