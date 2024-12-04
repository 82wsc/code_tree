import sys

y = int(sys.stdin.readline())

def y_year(n):
    if n%4!=0:
        return 'false'
    if n%100==0:
        return 'false'
    if n%400!=0:
        return 'false'

    return 'true'

print(y_year(y))