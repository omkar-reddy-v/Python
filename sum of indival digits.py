 print count of given indival digits in a number
n=int(input())
def count(n):
    count=0
    while (n>0):
        n=n//10
        count+=1
    print(count)
count(n)
