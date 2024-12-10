import sys

def palindrome(A):
    A_r = A[::-1]
    if A==A_r:
        print('Yes')
        
    else:
        print('No')
        

s = sys.stdin.readline().strip()

palindrome(s)