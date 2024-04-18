def sum_of_n(n):
    if n==0:return 0
    else:
        return n%10+sum_of_n(n//10)
n=int(input())
x=sum_of_n(n)
print(x)
