import sys

arr = tuple(map(int,sys.stdin.readline().split()))

def get_diff(i,j,k,l):
    sum1 = arr[i]+arr[j]
    sum2 = arr[k]+arr[l]
    sum3 = sum(arr)-sum1-sum2

    if sum1 == sum2 or sum1 == sum3 or sum2 == sum3:
        return None
    return max(sum1,sum2,sum3)-min(sum1,sum2,sum3)

ans = sys.maxsize
find = False

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(len(arr)):
            if k==i or k==j:
                continue
            for l in range(k+1,len(arr)):
                if l==i or l==j:
                    continue

                diff = get_diff(i,j,k,l)

                if get_diff(i,j,k,l)==0 or  get_diff(i,j,k,l) is None:
                    continue
                
                if diff<ans:
                    ans = diff
                    find = True

print(ans if find else -1)