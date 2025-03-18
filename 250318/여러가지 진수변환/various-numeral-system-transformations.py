import sys

n,b = map(int,sys.stdin.readline().split())
digits = []

while True:
    if n<b:
        digits.append(n)
        break

    digits.append(n%b)
    n //=b

for digit in digits[::-1]:
    print(digit,end="")