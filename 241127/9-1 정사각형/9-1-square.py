import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    for j in range(n):
        # 값을 순환시키며 계산
        value = (9 - (i * n + j) % 9)  # i*n+j를 기준으로 값 순환
        print(value, end="")
    print()  # 한 행 출력 후 줄바꿈

    
    