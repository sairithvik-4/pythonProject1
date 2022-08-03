print("Enter the how many terms required:")
n=int(input())
a=0
b=1
count=0
if n< 0:
    print("Enter a positive value")
elif n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    while count<=n:
        d=a+b
        print(b)
        a=b
        b=d
        count = count + 1