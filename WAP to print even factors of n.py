n=int(input())
i=1
while i<n:
    if n%i==0 and i%2==0:
        print(i)
    i+=1
print(i)
