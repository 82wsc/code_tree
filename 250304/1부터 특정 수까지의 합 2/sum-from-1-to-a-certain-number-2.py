n = int(input())

def num_sum(x):
    if x==0:
        return 0
    
    return num_sum(x-1) + x

print(num_sum(n))
