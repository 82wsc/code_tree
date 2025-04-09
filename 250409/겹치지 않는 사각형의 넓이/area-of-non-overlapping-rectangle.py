import sys

n = 3

segments = [
    tuple(map(int,sys.stdin.readline().split()))
    for _ in range(n)
]

print(segments)