for i in range(1, 19+1):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('buzz')

    elif i % 3 == 0:
        print("Fizz")
    else:
        print(f'{i}')
