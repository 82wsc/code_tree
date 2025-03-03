n,m = map(int,input().split())
A = list(map(int,input().split()))
q = [tuple(map(int,input().split())) for _ in range(m)]

def answer():
    global A
    r = 0
    for i in range(len(q)):
        print(sum(A[q[i][0]-1:q[i][1]]))

answer()