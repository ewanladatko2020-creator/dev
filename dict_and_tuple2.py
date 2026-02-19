def shopping_list():
    '''список покупок с ценами'''

    print('\n' + '=' * 40)
    print('🛒 СПИСОК ПОКУПОК С ЦЕНАМИ')
    print('=' * 40)

    # Словарь: продукт -> цена
    products = {}
    
    while True:
        print('\n' + '-' * 30)
        print('1. ➕ добавить продукт и цену')
        print('2. 📋 показать весь список')
        print('3. 🗑 удалить продукт')
        print('4. 💰 посчитать итоговую сумму')
        print('5. 🚪 выйти')
        print('-' * 30)

        choice = input('выбери (1-5): ').strip()

        if choice == '1':
            word = input('введите название продукта:').strip()
            if not word:
                print('ошибка! название товара не было введено')
                continue
            
            try:
                price = float(input('введите цену продукта:').strip())
                products[word] = price
                print(f'добавлен: {word} - {price} руб')

            except ValueError:
                print('должна быть введена цифра')
            pass

        elif choice == '2':
            if not products:
                print('названия продуктов отсутствуют')
            else:
                print('\n ПРОДУКТЫ')
                for product_name, product_price in products.items(): 
                    print(f'{product_name} : {product_price} руб')
            pass

        elif choice == '3':
            name_product = input('введите название искомого продукта').strip()

            if name_product in products:
                products.pop(name_product)
                print(f'продукт {name_product} удален')
            else:
                print(f'продукта {name_product} не было найдено')
            pass

        elif choice == '4':
            total = 0

            for price in products.values():
                total += price
            print(f'ИТОГО сумма составляет: {total}')
            pass

        elif choice == '5':
            print('👋 программа завершает работу...')
            break

        else:
            print('❌ неверный выбор! введите 1-5')

# Запускаем
shopping_list()