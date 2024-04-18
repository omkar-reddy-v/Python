def factors(n,i):
    if i>n:return 0
    if n%i==0:
        print(i,end=" ")
    factors(n,i+1)
n=int(input())
factors(n,i=1)
