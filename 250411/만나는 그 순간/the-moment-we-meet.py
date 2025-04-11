import sys

n,m = map(int,sys.stdin.readline().split())

max_r = 1000000

l_a = [0 for _ in range(max_r)]
l_b = [0 for _ in range(max_r)]

segments_a = [
    tuple(sys.stdin.readline().split())
    for _ in range(n)
]

segments_b = [
    tuple(sys.stdin.readline().split())
    for _ in range(m)
]


def func(segments,l):
    idx = 1
    for d,i in segments:
        i = int(i)
        
        if d=='R':
            for x in range(idx,idx+i):
                l[x] = l[x-1] + 1
            idx += i
                
        if d=='L':
            for x in range(idx,idx+i):
                l[x] = l[x-1] - 1
            idx += i
    return idx

idx_a = func(segments_a,l_a)
idx_b = func(segments_b,l_b)

end = min(idx_a, idx_b)

i = 1
found = False

while i < end:
    if l_a[i] == l_b[i]:
        found = True
        break
    i += 1

if found:
    print(i)
else:
    print(-1)

