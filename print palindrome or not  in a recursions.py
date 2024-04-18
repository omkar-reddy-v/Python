def palindrome(n):
    if n==0:return 0
    else:
        return 0+palindrome(n//10)
n=int(input())
x=palindrome(n)
print("palindrome" if x==n else "not palindrome")
