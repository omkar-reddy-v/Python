n=int(input())
i=1
sum=0
while i<n:
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print("perfect")
else:
    print("not perfect")
'''
perfect means:- sum factors existing that input number and sum and input number
is then output is "perfect" otherwise print "not perfect"
ex:-factors of 10
1,2,5,10
remove 10 and sum remaing factors
sum of factors means (1+2+5=8)
8==10 is it true or false
false then output is not perfect
ex2:-factors of 6
1,2,3,6
remove 6 and sum remaing factors
sum of factors is(1+2+3=6)
6==6 is it true or false
true so output excute "perfect"
'''
