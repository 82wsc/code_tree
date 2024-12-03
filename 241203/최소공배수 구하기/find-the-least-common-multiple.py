import sys

n,m = map(int,sys.stdin.readline().split())

def lcm(n,m):
    n_c, m_c = n,m
    if n<m:
        while n>0:
            temp=m
            m = n
            n = temp%n
        print(m*(n_c//m)*(m_c//m))
    else:
        while m>0:
            temp=n
            n = m
            m = temp%m
        print(n*(n_c//n)*(m_c//n))

lcm(n,m)

