import sys

m,d = map(int,sys.stdin.readline().split())


def date_test(x,y):
    if x>12:
        return 'No'  
    if y>31:
        return 'No'
    if x==2 and y>28:
        return 'No'
    if x%2==0 and y>30:
        return 'No'
    return 'Yes'


print(date_test(m,d))        
