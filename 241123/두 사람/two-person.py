import sys

a_age , a_sex = map(str, sys.stdin.readline().split())
b_age , b_sex = map(str, sys.stdin.readline().split())

if int(a_age)>=19 or int(b_age)>=19 or a_sex=='M' or b_sex=='M': 
    print(1)
else:
    print(0)