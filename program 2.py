#Sum of first N natural Number

# method 1
user_input = int(input('Enter the First Number: '))
value = 0
for i in range(1, user_input+1):
    value += i
print("sum of Natural numbers are ", value)

# method 2
n = int(input('Enter the First Number: '))
result = int((n * (n + 1)) / 2)
print(f"sum of Natural numbers are {result}")
