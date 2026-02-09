def text_analizer():
    '''аналзатор текста'''
    print('\n === анализатор текста ===')

    text = input('введите текст: \n')

    if not text:
        print('ошибка. введите текст')
        return

    print('\n' + '=' * 30 )
    print('= результаты анализа =')
    print('\n' + '=' * 30)
    
    total_chars = len(text)
    print(f'1. общее количество символов: {total_chars}')

    char_without_spaces = 0

    for char in text:
        if char != ' ':
            char_without_spaces += 1
    print(f'2. общее количество символов: {char_without_spaces}')

    word = text.split()
    word_count = len(word)
    print(f'3. разделенный текст и количество слов: {word} {word_count}')

    sentence_endings = ['.', '?', '...', '!']
    sentence_count = 0
    for char in text:
        if char in sentence_endings:
            sentence_count += 1
    if sentence_count == 0 and word_count > 0:
        sentence_count = 1

    print(f'4. итого предложений: {sentence_count}')
    
    if word:
        longest_word = max(word, key=len)
        print(f'5. самое длинное слово "{longest_word}" ({len(longest_word)} символов)')
        



text_analizer()

