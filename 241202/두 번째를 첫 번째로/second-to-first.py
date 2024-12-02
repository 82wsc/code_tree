import sys

s = sys.stdin.readline().strip()

f = s[0]


# replace 를 써야할 듯?
for i in s:
    if i==s[1]:
        s=s.replace(i,f)

print(s)