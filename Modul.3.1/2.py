a = int(input('введите диапозон чисел от: '))
b = int(input('до: '))

print('все числа диапозона: ')
for num_1 in range(a, b + 1):
    print(num_1)

print('все числа диапозона: ')
for num_2 in range (b, a -1, -1):
    print(num_2)

print('все числа кратные 7: ')
for num_3 in range (a, b +1):
    if num_3 % 7 == 0:
        print(num_3)
count = 0
for num_5 in range(a, b +1):
    if num_5 % 5 == 0:
        count +=1
print('количество чисел равных 5: ', count)
