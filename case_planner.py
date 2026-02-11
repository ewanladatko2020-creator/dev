def case_planner():
    '''анализирует список дел'''

    frist_task = int(1)
    twice_task = int(2)

    first_task = 'сходить в магазин'
    twice_task = 'сделать домашку'

    print('\n---какое дело вы хотите запланировать?---')
    print(f'1. {first_task}')
    print(f'2. {twice_task}')

    try:

        choice = int(input('какой выбор вы хотите сделать(1/2)?').strip())
        if choice == 1:
            task_name = first_task
        elif choice == 2:
            task_name = twice_task
        else:
            print('выбор не сделан! по умолчанию выбирается задача"сходить в магазин"')
            task_name = first_task

        print('\n---планирование---')

        difficulty = int(input('оцените сложность (1-10):').strip())
        execution_time = float(input('сколько времени займет(часов):').strip())
        urgently = input('срочно? (да/нет)').strip().lower()

        is_urgent = urgently == 'да'

        print('\n' + '=' * 40)
        print('РЕЗУЛЬТАТЫ АНАЛИЗА')
        print('=' * 40)

        print(f'дело: {task_name}')
        print(f"сложность: {difficulty} / 10 ({'высокая' if difficulty >= 7 else 'средняя' if difficulty >= 4 else 'низкая'})")
        print(f'сколько времени заняло: {execution_time}')
        print(f"срочно: {'да' if is_urgent else 'нет'}")
    except:
        print('ошибка! введите значение')


case_planner()


        


