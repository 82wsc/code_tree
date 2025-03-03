n, m = map(int,input().split())
A = list(map(int,input().split()))

def dev_sum(m):
    r=0
    while m!=0:
        r+=A[m-1]
        if m%2==0:
            m//=2
        else:
            m-=1
    print(r)    

dev_sum(m)