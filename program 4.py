# prime numbers
n = int(input("enter the number to check: "))
count = 0
a = n//2
for i in range(2, a+1):
    if n % i == 0:
        print("not prime")
        count = 1
        break
if count == 0:
    print("prime Number")