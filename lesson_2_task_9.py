maxi = 0
while True:
    try:
        integer_number = int(input('Введите целое число: '))
        break
    except ValueError:
        print('''Надо вводить целые числа.(Для работы программы запрещен
ввод слов, дробей, чисел с плавающей точкой)''')
integer_number = abs(integer_number)
while integer_number > 0:
    if integer_number % 10 > maxi:
        maxi = integer_number % 10
    integer_number = integer_number // 10
print ('Самая большая цифра в числе:', maxi)