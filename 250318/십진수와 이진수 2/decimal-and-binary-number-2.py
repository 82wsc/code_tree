import sys

n = int(sys.stdin.readline(),2)
n*=17
digits = []

while True:
    if n<2:
        digits.append(n)
        break

    digits.append(n%2)
    n//=2

for digit in digits[::-1]:
    print(digit,end="")