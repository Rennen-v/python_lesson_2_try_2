mult = 1
while True:
    try:
        ints_number = int(input('Введите целое число: '))
        break
    except ValueError:
        print('''Надо вводить целые числа.(Для работы программы запрещен
ввод слов, дробей, чисел с плавающей точкой)''')
ints_number = abs(ints_number)
while ints_number > 0:
    mult *= ints_number % 10
    ints_number = ints_number // 10
print('Произведение цифр числа равна:', mult)