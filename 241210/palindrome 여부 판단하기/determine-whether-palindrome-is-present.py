import sys

def palindrome(A):
    if A==A[::-1]:
        print('Yes')
        
    else:
        print('No')
        

s = sys.stdin.readline()

palindrome(s)