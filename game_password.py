def password():
    '''игра угадай пароль'''

    print('\n' + '=' * 40)
    print('игра угадай пароль')
    print('=' * 40)
    
    max_attempts = 5
    attempts = 0
    count_input = []
    while attempts < max_attempts:

        password = 'qwerty123'

        input_text = input(f'введите пароль: \n попытка {attempts + 1} из {max_attempts}:').strip()

        count_input.append(input_text)

        if not input_text:
            print('пароль не был введен! попробуйте еще раз')
            count_input.pop()#удаление пустого ввода
            continue
        attempts += 1

        if password == input_text:
            print('пароль верный')
            print(f'попыток: {attempts}')
            return False
        else:
            incorrect_input = max_attempts - attempts
            
        if len(input_text) != len(password):
            print(f'пароль не верный! подсказка: длина пароля: {len(password)}')
        elif input_text.lower() == password.lower():
            print(f'пароль не верный! проверьте регистр пароля')
        else:
            print('пароль не верный')

        if incorrect_input > 0:
            print(f'осталось попыток {incorrect_input}')
        else:
            print('\n' + '=' * 60)
            print(f'вход временно заблокирован! правильный пароль был {password}')
            print('=' * 60)
            return False
    return False
            


        
password()
        
    



