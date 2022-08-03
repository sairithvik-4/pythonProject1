n=int(input('enter the number:'))
fac=0
for i in range (1 , n):
    if n%i==0:
        fac=fac+1
if(fac>1):
    print('number is not prime')
else:
    print('number is prime')