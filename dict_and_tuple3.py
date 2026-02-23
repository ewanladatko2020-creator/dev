def phonebook_advanced():

    '''телефонная книга'''

    print('\n' + '=' * 50)
    print('телефонная книга с группами')
    print('=' * 50)

    contacts = {}

    while True:
        print('\n' + '-' * 40)
        print('1. ➕ добавить контакт')
        print('2. 📋 показать все контакты')
        print('3. 🔍 поиск по имени')
        print('4. 🗑 удалить контакт')
        print('5. 📂 показать группу')
        print('6. 📊 статистика')
        print('7. 🚪 выйти')
        print('-' * 40)

        choice = input('выбери число (1-7)').strip()

        if choice == '1':

            contact = input('введите имя пользователя: ').strip()
            phone_number = input('введите номер телефона: ').strip()
            group = input('выбери группу контакта (семья/друзья/работа): ').strip()

            contacts[contact] = {'phone_number' : phone_number, 'group' : group}
            print(f'контакт {contact} добавлен')
            # ТВОЯ ОЧЕРЕДЬ: добавить контакт
            # 1. Спросить имя
            # 2. Спросить телефон
            # 3. Спросить группу (семья/друзья/работа)
            # 4. Сохранить как contacts[имя] = {'phone_number': телефон, 'group': группа}
            pass
            
        elif choice == '2':
            if not contacts:
                print('список контактов пуст')
                continue
            else:
                print(contacts)
            # ТВОЯ ОЧЕРЕДЬ: показать все контакты
            # 1. Если список пуст - сообщить
            # 2. Иначе показать все контакты с группами
            pass
            
        elif choice == '3':
            search_name = input('введите искомое имя: ').strip()

            if search_name in contacts:
                info = contacts[search_name]
                print(f'имя: {search_name}, телефон:{info["phone_number"]}, группа: {info["group"]}')

            else:
                print(f'контакт {search_name} не найден')
            # ТВОЯ ОЧЕРЕДЬ: поиск по имени
            # 1. Спросить имя для поиска
            # 2. Если нашли - показать телефон и группу
            # 3. Если нет - сообщить
            pass
            
        elif choice == '4':
            pop_contacts = input('введите контакт который вы хотите удалить: ').strip()

            if pop_contacts in contacts:
                contacts.pop(pop_contacts)
                print(f'контакт {pop_contacts} успешно удален')
            else:
                print(f'контакт {pop_contacts} не найден')
            # ТВОЯ ОЧЕРЕДЬ: удалить контакт
            # 1. Спросить имя
            # 2. Если есть - удалить
            pass
            
        elif choice == '5':
            name_group = input('введите название группы: ').strip()

            for name, info in contacts.items():
                if info['group'] == name_group:
                    print(f'{name} : {info["phone_number"]}')
            # ТВОЯ ОЧЕРЕДЬ: показать группу
            # 1. Спросить название группы
            # 2. Показать все контакты из этой группы
            pass
            
        elif choice == '6':
            print('\n' + '=' * 40)
            print('статистика')
            print('=' * 40)

            statistic = len(contacts)
            print(f'всего контактов {statistic}')
            # ТВОЯ ОЧЕРЕДЬ: статистика
            # 1. Сколько всего контактов
            # 2. Сколько в каждой группе
            pass
            
        elif choice == '7':
            print('👋 программа завершает работу...')
            break
            
        else:
            print('❌ неверный выбор!')

phonebook_advanced()