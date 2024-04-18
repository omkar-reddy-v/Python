def sum_of_odd_factors(n,i):
    if i>n:return 0
    if n%i==0 and i%2!=0:
        return i+sum_of_odd_factors(n,i+1)
    else:
        return sum_of_odd_factors(n,i+1)
n=int(input())
x=sum_of_odd_factors(n,i=1)
print(x)
