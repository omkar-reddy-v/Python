def count_of_factors(n,i):
    if i>n:return 0
    if n%i==0:
        return 1+count_of_factors(n,i+1)
    else:
        return count_of_factors(n,i+1)
n=int(input())
x=count_of_factors(n,i=1)
print(x)
