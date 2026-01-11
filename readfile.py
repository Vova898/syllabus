def read_disciplines_from_file(filename):
    '''Чтение дисциплин из текстового файла'''
    disciplines = []
    
    try:
        # Открываем файл для чтения
        with open(filename, 'r', encoding='utf-8') as file:
            line_number = 0
            for line in file:
                line_number += 1
                line = line.strip()
                # Пропускаем пустые строки
                if not line:
                    continue
                # Разделяем строку по разделителю ';'
                parts = line.split(';')
                

                # Проверяем корректность формата
                if len(parts) != 6:
                    print(f"Ошибка в строке {line_number}: неверный формат (ожидается 6 полей, получено {len(parts)})")
                    return None
                name = parts[0].strip()
                start_semester_str = parts[1].strip()
                duration_str = parts[2].strip()
                total_hours_str = parts[3].strip()
                assessment_type = parts[4].strip()
                department = parts[5].strip()
                
                # Проверяем корректность числовых значений
                try:
                    start_semester = int(start_semester_str)
                    duration = int(duration_str)
                    total_hours = int(total_hours_str)
                except ValueError:
                    print(f"Ошибка в строке {line_number}: числовые поля должны быть целыми числами")
                    return None
                
                if assessment_type not in ['зачет', 'экзамен']:
                    print(f"Ошибка в строке {line_number}: неверный вид отчетности '{assessment_type}' (допустимо: 'зачет' или 'экзамен')")
                    return None
                
                # Создаем объект дисциплины и добавляем в список
                discipline = Discipline(name, start_semester, duration, total_hours, assessment_type, department)
                disciplines.append(discipline)
        
        # Проверяем, что в файле не менее 25 дисциплин
        if len(disciplines) < 25:
            print(f"Ошибка: в файле должно быть не менее 25 дисциплин, а найдено {len(disciplines)}")
            return None
        
        print(f"Успешно загружено {len(disciplines)} дисциплин из файла '{filename}'")
        return disciplines
        
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла '{filename}': {e}")
        return None

