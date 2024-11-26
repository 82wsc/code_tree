import sys

n = int(sys.stdin.readline().strip())

# 위쪽 출력
for i in range(1, n + 1):
    if i % 2 == 1:  # 홀수 줄
        print(' '.join('*' * (n-(i//2))))
    else:  # 짝수 줄
        print(' '.join('*' * (i//2)))

# 아래쪽 출력
for i in range(n,0,-1):
    if i % 2 == 1:  # 홀수 줄
        print(' '.join('*' * (n-(i//2))))
    else:  # 짝수 줄
        print(' '.join('*' * (i//2)))

