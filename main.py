operation = int(input('1.Сложение \n2.Вычитание \n3.Умножение \n4.Деление \nВведите номер операции: '))
fn = int(input('Введите первое число: '))
sn = int(input('Введите второе число: '))
if operation == 1:
    print(fn, '+', sn, '=', fn+sn)
elif operation == 2:
    print(fn, '-', sn, '=', fn-sn)
elif operation == 3:
    print((fn, '*', sn, '=', fn*sn))
elif operation == 4:
    print((fn, '/', sn, '=', fn//sn))
else:
    print('Неверная операция')