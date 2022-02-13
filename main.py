lang = int(input('1.Russian \n2.English \n'))
if lang == 2:
    operation = int(input('1.Addition \n2.Subtraction \n3.Multiplication \n4.Division '
                          '\nEnter operation number: '))
    fn = int(input('Enter first number: '))
    sn = int(input('Enter second number: '))
    if operation == 1:
        print(fn, '+', sn, '=', fn + sn)
    elif operation == 2:
        print(fn, '-', sn, '=', fn - sn)
    elif operation == 3:
        print((fn, '*', sn, '=', fn * sn))
    elif operation == 4:
        print((fn, '/', sn, '=', fn // sn))
    else:
        print('Error')
else:
    operation = int(input('1.Сложение \n2.Вычитание \n3.Умножение \n4.Деление \nВведите номер операции: '))
    fn = int(input('Введите первое число: '))
    sn = int(input('Введите второе число: '))
    if operation == 1:
        print(fn, '+', sn, '=', fn + sn)
    elif operation == 2:
        print(fn, '-', sn, '=', fn - sn)
    elif operation == 3:
        print(fn, '*', sn, '=', fn * sn)
    elif operation == 4:
        print(fn, '/', sn, '=', fn // sn)
    else:
        print('Неверная операция')
