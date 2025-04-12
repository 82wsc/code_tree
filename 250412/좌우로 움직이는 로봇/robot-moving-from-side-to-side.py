import sys

n,m = map(int,sys.stdin.readline().split())

max_r = 1000000

d_a, d_b = [0 for _ in range(max_r)], [0 for _ in range(max_r)] 

def func(dis,num):
    idx = 1
    for _ in range(num):
        i,d = sys.stdin.readline().split()
        i = int(i)

        if d=='R':
            for x in range(idx,idx+i):
                dis[x] = dis[x-1] + 1
            idx += i

        if d=='L':
            for x in range(idx,idx+i):
                dis[x] = dis[x-1] - 1
            idx += i
    
    dis[idx:] = [dis[idx-1]] * (len(dis) - idx)

    return idx

end_a = func(d_a,n)
end_b = func(d_b,m)

end = max(end_a,end_b)

cnt = 0
for i in range(1,end):
    if (d_a[i-1]!=d_b[i-1]) and (d_a[i]==d_b[i]):
        cnt+=1

print(cnt)

