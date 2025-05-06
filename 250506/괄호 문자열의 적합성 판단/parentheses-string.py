import sys

def func(s):
    stack = []

    d = {')':'('}
    for i in s:
        if i in d.values():
            stack.append(i)
        elif i in d.keys():
            if not stack or stack[-1] != d[i]:
                return False
            stack.pop()
    return not stack

s = sys.stdin.readline()

if func(s):
    print('Yes')
else:
    print('No')
