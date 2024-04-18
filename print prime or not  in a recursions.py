def prime(n,i):
    if i>n:return 0
    if n%i==0:
        return 1+prime(n,i+1)
    else:
        return prime(n,i+1)
n=int(input())
x=prime(n,i=1)
print("prime" if x==2 and n%2==0 else "not prime")
