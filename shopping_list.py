shopping_list = ['хлеб', 'молоко', 'яйца']

is_runing = True

print('добро пожаловать в список покупок')

while is_runing:

    print('\n' + '=' * 30)
    print('1. показать текущий список товаров')
    print('2. добавить товар в конец списка')
    print('3. удалить товар с конца списка')
    print('4. выйти из программы')
    print('=' * 30)

    choice = input('введите из вышеуказанного списка цифру(1-4)').strip()

    if choice == '1':
        print('список покупок')
        print(shopping_list)
    elif choice == '2':
        new_item = input('введите товар')
        shopping_list.append(new_item)
    elif choice == '3':
        print('удаляем товар...')
        shopping_list.pop()
    elif choice == '4':
        print('выход из программы')
        is_runing = False

    else:
        
        print('введено неверное значение или символ')



 