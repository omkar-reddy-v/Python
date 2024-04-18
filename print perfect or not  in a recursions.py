def perfect(n,i):
    if i==n:return 0
    if n%i==0:
        return i+perfect(n,i+1)
    else:
        return perfect(n,i+1)
n=int(input())
x=perfect(n,i=1)
print("perfect" if x==n else "not perfect")
