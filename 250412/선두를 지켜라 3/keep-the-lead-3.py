import sys

n,m = map(int,sys.stdin.readline().split())

max_r = 1000000

d_a, d_b = [0 for _ in range(max_r)], [0 for _ in range(max_r)]


def func(dis,c):
    idx = 1
    # v,t
    for i in range(c):
        v,t = map(int, sys.stdin.readline().split())

        for x in range(idx,idx+t):
            dis[x] = dis[x-1] + v
        
        idx += t
    
    return idx

end_a = func(d_a,n)
end_b = func(d_b,m)

end = min(end_a, end_b)

cnt = 0
for i in range(1,end):
    if (d_a[i-1]>=d_b[i-1]) and (d_a[i]<d_b[i]):
        cnt +=1

    elif (d_a[i-1] <= d_b[i-1]) and (d_a[i]>d_b[i]):
        cnt+=1

    elif ((d_a[i-1] < d_b[i-1])) and (d_a[i]==d_b[i]):
        cnt+=1

    elif ((d_a[i-1] > d_b[i-1])) and (d_a[i]==d_b[i]):
        cnt+=1

print(cnt)