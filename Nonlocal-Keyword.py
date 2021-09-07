def outer():
    first_num = 1
    def inner():
        nonlocal first_num
        first_num = 0
        second_num = 1
        print('inner - second number is ', second_num)
    inner()
    print('outer - first number is  ', first_num)

outer()