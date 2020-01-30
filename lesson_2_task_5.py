while True:
    try:
        ints_number = int(input('Введите целое число: '))
        break
    except ValueError:
        print('''Надо вводить целые числа.(Для работы программы запрещен
ввод слов, дробей, чисел с плавающей точкой)''')

while ints_number>0:
     print(ints_number%10)
     ints_number = ints_number//10
