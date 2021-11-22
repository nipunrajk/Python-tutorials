#sum of Natural Numbers in a given range
a = int(input('Enter the starting Number '))
b = int(input('Enter the Ending Number '))
value = 0
for i in range(a, b+1):
    value += i
print(f"sum of natural Number is {value}")