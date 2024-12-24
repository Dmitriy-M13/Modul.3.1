num_1 = int(input('введите диапозон чисел от: '))
num_2 = int(input('до: '))

for i in range (num_1, num_2 +1):
    if i % 7 == 0:
        print(i)
