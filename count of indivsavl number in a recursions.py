def count_of_digits(n):
    if n==0:
        return 0
    else:
        return 1+count_of_digits(n//10)
n=int(input())
x=count_of_digits(n)
print(x)
