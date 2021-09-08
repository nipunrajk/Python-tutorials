# fizz_buzz algorithm
# if divisible by 3 => Fizz
# if divisible by 5 => Buzz
# if divisible by 3 and 5 => FizzBuzz
# if any other no => given number

def fizz_buzz(input):
    if (input % 5 == 0 ) and (input % 3 == 0):
        return "FizzBuzz"
    if (input % 3 ==0):
        return "Fizz"
    if (input % 5 == 0):
        return "Fizz"
    return input


print(fizz_buzz(3))