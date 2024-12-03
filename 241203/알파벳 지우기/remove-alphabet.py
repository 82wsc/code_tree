import sys

a = list(sys.stdin.readline().strip())
b = list(sys.stdin.readline().strip())

a = [i for i in a if i.isdigit()]
b = [i for i in b if i.isdigit()]

a = int(''.join(a))
b = int(''.join(b))

print(a+b)