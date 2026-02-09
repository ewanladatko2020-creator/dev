def grades_analizer():
    '''анализатор оценок'''

    print('\n === АНАЛИЗАТОР ОЦЕНОК ===')

    input_text = input('введите оценки:').strip()

    if not input_text:
        print('оценки не были введены')
        return
    
    raw_gardes = input_text.split(',')

    grades = []

    for grades_str in raw_gardes:
        clean_grades = grades_str.strip()
        if clean_grades:
            try:
                grade = int(clean_grades)
                if 2 <= grade <= 5:
                    grades.append(grade)
                else:
                    print(f'пропускаем {clean_grades} оценка должна быть от 2 до 5')
            except ValueError:
                print(f'пропускаем {clean_grades} это не число')

    if not grades:
        print('нет оценок для анализа')
        return
    
    print('\n' + '=' * 40)
    print('РЕЗУЛЬТАТЫ АНАЛИЗА')
    print('=' * 40)

    print(f'оценки {grades}')

    total_grades = len(grades)
    print(f'всего оценок: {total_grades}')

    total_sum = 0
    for grade in grades:
        total_sum += grade

    average = total_sum / total_grades
    print(f'средняя оценка: {average:.2f}')

    max_grade = max(grades)
    print(f'наивысшая оценка {max_grade}')

    min_grade = min(grades)
    print(f'наменьшая оценка{min_grade}')

# счетчик оценок 
    grade_2 = 0
    grade_3 = 0
    grade_4 = 0
    grade_5 = 0

    for current_grade in grades:

        if current_grade == 2:
            grade_2 += 1
        elif current_grade == 3:
            grade_3 += 1
        elif current_grade == 4:
            grade_4 += 1
        elif current_grade == 5:
            grade_5 += 1

    print('\n распределитель оценок')
    print(f'оценок 2 всего {grade_2}')
    print(f'оценок 3 всего {grade_3}')
    print(f'оценок 4 всего {grade_4}')
    print(f'оценок 5 всего {grade_5}')


grades_analizer()

