def basic_calculator():

    print('\n--обычный калькулятор--')

    try:
        num1 = float(input('введите первое число:'))

        print('введите доступные операции: +, -, /, //, %, *, **')
        operation = input('введите операцию: ').strip()

        num2 = float(input('введите второе число:'))

        result = None

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print('на 0 делить нельзя!')
                return
        elif operation == '//':
            if num2 != 0:
                result = num1 // num2
            else:
                print('на 0 делить нельзя!')
                return
        elif operation == '*':
            result = num1 * num2
        elif operation == '**':
            result = num1 ** num2
        elif operation == '%':
            if num2 != 0:
                result = num1 % num2
            else:
                print('на 0 делить нельзя!')
        else:
            print('ошибка')
            return

        print(f'результат: {num1} {operation} {num2} = {result}')

    except ValueError: 
        print('введите число или символ')

basic_calculator()

#надо дописать код есть ошибки