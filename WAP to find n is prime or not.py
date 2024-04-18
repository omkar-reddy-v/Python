n=int(input())
i=1
count=0
while i<=n:
    if n%i==0:
        count+=i
    i+=1
if count==2:
    print("prime")
else:
    print("not prime")
'''
*prime number means which number got count of facotrs is 2 it is called prime number
*composite number means which number got count of facotrs is more than 2 it is called
composite numbers
*either the given number is got the less than 2 facotrs it is called
either prime or composite number
'''
