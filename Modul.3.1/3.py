a = int(input('введите диапозон чисел от: '))
b = int(input('до: '))

for i in range(a, b +1):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizz Buzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
