class Discipline:
    '''Класс для хранения информации об одной дисциплине'''
    
    def __init__(self, name, start_semester, duration, total_hours, assessment_type, department):
        '''Конструктор класса Discipline'''

        self.name = name
        self.start_semester = int(start_semester)
        self.duration = int(duration)
        self.total_hours = int(total_hours)
        self.assessment_type = assessment_type
        self.department = department
    
    def __str__(self):
        '''Возвращает строковое представление дисциплины для вывода'''
        return f"{self.name:30} | {self.start_semester:2} | {self.duration:2} | {self.total_hours:4} | {self.assessment_type:10} | {self.department}"
    
    def to_file_string(self):
        '''Возвращает строковое представление дисциплины для записи в файл'''
        return f"{self.name};{self.start_semester};{self.duration};{self.total_hours};{self.assessment_type};{self.department}"


def binary_insertion_sort(arr, key_func):
    '''Сортировка бинарными вставками'''
    # Если массив пуст или содержит один элемент, он уже отсортирован
    if len(arr) <= 1:
        return arr[:]
    # Создаем копию массива для сортировки
    sorted_arr = arr[:]
    # Проходим по всем элементам начиная со второго
    for i in range(1, len(sorted_arr)):
        current = sorted_arr[i]
        current_key = key_func(current)
        
        # Бинарный поиск позиции для вставки в отсортированной части
        left = 0
        right = i - 1
        while left <= right:
            mid = (left + right) // 2
            mid_key = key_func(sorted_arr[mid])
            
            if current_key < mid_key:
                right = mid - 1
            else:
                left = mid + 1
        # Сдвигаем элементы вправо, чтобы освободить место для вставки
        for j in range(i - 1, left - 1, -1):
            sorted_arr[j + 1] = sorted_arr[j]
        # Вставляем текущий элемент на найденную позицию
        sorted_arr[left] = current
    
    return sorted_arr


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


def write_report_to_file(filename, report_title, disciplines, report_type):
    '''Запись отчета в файл'''
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write("=" * 80 + "\n")
            file.write(report_title + "\n")
            file.write("=" * 80 + "\n\n")
            
            # Записываем заголовок таблицы в зависимости от типа отчета
            if report_type == 1:
                file.write("Полный список всех дисциплин, отсортированный по: семестр(↑), кафедра(↑), часы(↓)\n")
            elif report_type == 2:
                file.write("Список дисциплин с заданным видом отчётности, отсортированный по: длительность(↑), часы(↓)\n")
            elif report_type == 3:
                file.write("Список дисциплин с общим количеством часов от N1 до N2, отсортированный по: кафедра(↑), часы(↓)\n")
            file.write("-" * 80 + "\n")
            
            # Записываем заголовки столбцов
            file.write(f"{'№':3} | {'Название дисциплины':30} | {'Сем':4} | {'Длит':4} | {'Часы':6} | {'Отчетность':10} | {'Кафедра':20}\n")
            file.write("-" * 80 + "\n")
            
            # Записываем данные о дисциплинах
            for i, disc in enumerate(disciplines, 1):
                file.write(f"{i:3} | {disc.name:30} | {disc.start_semester:4} | {disc.duration:4} | {disc.total_hours:6} | {disc.assessment_type:10} | {disc.department:20}\n")
            # Записываем итоговую информацию
            file.write("-" * 80 + "\n")
            file.write(f"Всего дисциплин: {len(disciplines)}\n\n\n")
        print(f"Отчет успешно сохранен в файл '{filename}'")   
    except Exception as e:
        print(f"Ошибка при записи в файл '{filename}': {e}")


def generate_report1(disciplines):
    '''Генерация отчета 1: Полный список всех дисциплин'''
    print("\n" + "=" * 80)
    print("ГЕНЕРАЦИЯ ОТЧЕТА 1")
    print("Полный список всех дисциплин")
    print("Сортировка: семестр(↑), кафедра(↑), часы(↓)")
    print("=" * 80)
    
    # Определяем функцию ключа для сортировки
    def sort_key(disc):
        '''Ключ сортировки: семестр (по возрастанию), кафедра (по возрастанию), часы (по убыванию)'''
        return (disc.start_semester, disc.department, -disc.total_hours)
    # Сортируем дисциплины с помощью бинарных вставок
    sorted_disciplines = binary_insertion_sort(disciplines, sort_key)
    # Выводим результат на экран
    print(f"{'№':3} | {'Название дисциплины':30} | {'Сем':4} | {'Длит':4} | {'Часы':6} | {'Отчетность':10} | {'Кафедра':20}")
    print("-" * 80)
    
    for i, disc in enumerate(sorted_disciplines, 1):
        print(f"{i:3} | {disc.name:30} | {disc.start_semester:4} | {disc.duration:4} | {disc.total_hours:6} | {disc.assessment_type:10} | {disc.department:20}")
    print("=" * 80)
    print(f"Всего дисциплин: {len(sorted_disciplines)}")
    return sorted_disciplines


def generate_report2(disciplines, assessment_type):
    '''Генерация отчета 2: Дисциплины с заданным видом отчётности'''

    print(f"\n" + "=" * 80)
    print("ГЕНЕРАЦИЯ ОТЧЕТА 2")
    print(f"Дисциплины с видом отчётности: '{assessment_type}'")
    print("Сортировка: длительность(↑), часы(↓)")
    print("=" * 80)
    
    # Фильтруем дисциплины по виду отчетности
    filtered_disciplines = []
    for disc in disciplines:
        if disc.assessment_type == assessment_type:
            filtered_disciplines.append(disc)
    # Проверяем, есть ли дисциплины с заданным видом отчетности
    if not filtered_disciplines:
        print(f"Нет дисциплин с видом отчётности '{assessment_type}'")
        return []
    # Определяем функцию ключа для сортировки
    def sort_key(disc):
        '''Ключ сортировки: длительность (по возрастанию), часы (по убыванию)'''
        return (disc.duration, -disc.total_hours)
    sorted_disciplines = binary_insertion_sort(filtered_disciplines, sort_key)
    print(f"{'№':3} | {'Название дисциплины':30} | {'Сем':4} | {'Длит':4} | {'Часы':6} | {'Отчетность':10} | {'Кафедра':20}")
    print("-" * 80)
    
    for i, disc in enumerate(sorted_disciplines, 1):
        print(f"{i:3} | {disc.name:30} | {disc.start_semester:4} | {disc.duration:4} | {disc.total_hours:6} | {disc.assessment_type:10} | {disc.department:20}")
    
    print("=" * 80)
    print(f"Найдено дисциплин: {len(sorted_disciplines)}")
    
    return sorted_disciplines


def generate_report3(disciplines, n1, n2):
    '''Генерация отчета 3: Дисциплины с общим количеством часов от N1 до N2'''
    print(f"\n" + "=" * 80)
    print("ГЕНЕРАЦИЯ ОТЧЕТА 3")
    print(f"Дисциплины с количеством часов от {n1} до {n2}")
    print("Сортировка: кафедра(↑), часы(↓)")
    print("=" * 80)
    
    # Фильтруем дисциплины по диапазону часов
    filtered_disciplines = []
    for disc in disciplines:
        if n1 <= disc.total_hours <= n2:
            filtered_disciplines.append(disc)
    if not filtered_disciplines:
        print(f"Нет дисциплин с количеством часов от {n1} до {n2}")
        return []
    
    # Определяем функцию ключа для сортировки
    def sort_key(disc):
        '''Ключ сортировки: кафедра (по возрастанию), часы (по убыванию)'''
        return (disc.department, -disc.total_hours)
    
    # Сортируем отфильтрованные дисциплины с помощью бинарных вставок
    sorted_disciplines = binary_insertion_sort(filtered_disciplines, sort_key)
    print(f"{'№':3} | {'Название дисциплины':30} | {'Сем':4} | {'Длит':4} | {'Часы':6} | {'Отчетность':10} | {'Кафедра':20}")
    print("-" * 80)
    
    for i, disc in enumerate(sorted_disciplines, 1):
        print(f"{i:3} | {disc.name:30} | {disc.start_semester:4} | {disc.duration:4} | {disc.total_hours:6} | {disc.assessment_type:10} | {disc.department:20}")
    
    print("=" * 80)
    print(f"Найдено дисциплин: {len(sorted_disciplines)}")
    return sorted_disciplines


def show_all_disciplines(disciplines):
    '''Вывод всех дисциплин без сортировки'''

    print("\n" + "=" * 80)
    print("ВСЕ ДИСЦИПЛИНЫ (БЕЗ СОРТИРОВКИ)")
    print("=" * 80)
    
    print(f"{'№':3} | {'Название дисциплины':30} | {'Сем':4} | {'Длит':4} | {'Часы':6} | {'Отчетность':10} | {'Кафедра':20}")
    print("-" * 80)
    
    for i, disc in enumerate(disciplines, 1):
        print(f"{i:3} | {disc.name:30} | {disc.start_semester:4} | {disc.duration:4} | {disc.total_hours:6} | {disc.assessment_type:10} | {disc.department:20}")
    
    print("=" * 80)
    print(f"Всего дисциплин: {len(disciplines)}")


def main():
    """Основная функция программы"""
    print("=" * 60)
    print("ПРОГРАММА 'УЧЕБНЫЙ ПЛАН'")
    print("=" * 60)
    print("Все отчеты будут сохранены в файл 'output.txt'")
    print("=" * 60)
    disciplines = read_disciplines_from_file('input.txt')
    if disciplines is None:
        print("Программа завершена из-за ошибки чтения файла.")
        return
    
    #Menu
    while True:
        print("\n" + "=" * 60)
        print("ГЛАВНОЕ МЕНЮ")
        print("=" * 60)
        print("1. Показать все дисциплины (без сохранения)")
        print("2. Создать отчет 1: Полный список (семестр↑, кафедра↑, часы↓)")
        print("3. Создать отчет 2: По виду отчетности (длительность↑, часы↓)")
        print("4. Создать отчет 3: По диапазону часов (кафедра↑, часы↓)")
        print("5. Создать все отчеты и сохранить в output.txt")
        print("6. Выход")
        print("=" * 60)
        choice = input("Выберите пункт меню (1-6): ").strip()
        
        if choice == "1":
            show_all_disciplines(disciplines)
            
        elif choice == "2":
            report1_result = generate_report1(disciplines)
            save_choice = input("\nСохранить этот отчет в файл output.txt? (да/нет): ").strip().lower()
            if save_choice in ['да', 'д', 'y', 'yes']:
                try:
                    open('output.txt', 'w', encoding='utf-8').close()
                except:
                    pass
                write_report_to_file('output.txt', 
                                    'ОТЧЕТ 1: Полный список всех дисциплин', 
                                    report1_result, 
                                    1)
            
        elif choice == "3":
            print("\nДоступные виды отчетности: зачет, экзамен")
            assessment = input("Введите вид отчетности: ").strip().lower()
            if assessment not in ['зачет', 'экзамен']:
                print("Ошибка: допустимые значения - 'зачет' или 'экзамен'")
                continue
            report2_result = generate_report2(disciplines, assessment)
            if report2_result:
                save_choice = input("\nСохранить этот отчет в файл output.txt? (да/нет): ").strip().lower()
                if save_choice in ['да', 'д', 'y', 'yes']:
                    write_report_to_file('output.txt', 
                                        f'ОТЧЕТ 2: Дисциплины с видом отчётности "{assessment}"', 
                                        report2_result, 
                                        2)
            
        elif choice == "4":
            try:
                n1 = int(input("Введите минимальное количество часов (N1): "))
                n2 = int(input("Введите максимальное количество часов (N2): "))
                if n1 < 0 or n2 < 0:
                    print("Ошибка: количество часов не может быть отрицательным")
                    continue
                if n1 > n2:
                    print("Ошибка: N1 должно быть меньше или равно N2")
                    continue
                report3_result = generate_report3(disciplines, n1, n2)
                # Если есть результаты, спрашиваем о сохранении
                if report3_result:
                    save_choice = input("\nСохранить этот отчет в файл output.txt? (да/нет): ").strip().lower()
                    if save_choice in ['да', 'д', 'y', 'yes']:
                        # Записываем отчет в файл
                        write_report_to_file('output.txt', 
                                            f'ОТЧЕТ 3: Дисциплины с количеством часов от {n1} до {n2}', 
                                            report3_result, 
                                            3)
                        
            except ValueError:
                print("Ошибка: введите целые числа для N1 и N2")
                
        elif choice == "5":
            try:
                open('output.txt', 'w', encoding='utf-8').close()
            except:
                pass
            
            print("\nСоздание всех отчетов...")
            # Отчет 1
            print("\n1. Создание отчета 1...")
            report1_result = generate_report1(disciplines)
            write_report_to_file('output.txt', 
                                'ОТЧЕТ 1: Полный список всех дисциплин', 
                                report1_result, 
                                1)
            
            # Отчет 2 (для зачетов)
            print("\n2. Создание отчета 2 для 'зачет'...")
            report2_zachet = generate_report2(disciplines, 'зачет')
            write_report_to_file('output.txt', 
                                'ОТЧЕТ 2: Дисциплины с видом отчётности "зачет"', 
                                report2_zachet, 
                                2)
            
            # Отчет 2 (для экзаменов)
            print("\n3. Создание отчета 2 для 'экзамен'...")
            report2_exam = generate_report2(disciplines, 'экзамен')
            write_report_to_file('output.txt', 
                                'ОТЧЕТ 2: Дисциплины с видом отчётности "экзамен"', 
                                report2_exam, 
                                2)
            
            # Отчет 3 (для диапазона 0-100 часов)
            print("\n4. Создание отчета 3 для часов 50-100...")
            report3_50_100 = generate_report3(disciplines, 0, 100)
            write_report_to_file('output.txt', 
                                'ОТЧЕТ 3: Дисциплины с количеством часов от 50 до 100', 
                                report3_50_100, 
                                3)
            
            # Отчет 3 (для диапазона 100-10000 часов)
            print("\n5. Создание отчета 3 для часов 100-200...")
            report3_100_200 = generate_report3(disciplines, 100, 10000)
            write_report_to_file('output.txt', 
                                'ОТЧЕТ 3: Дисциплины с количеством часов от 100 до 200', 
                                report3_100_200, 
                                3)
            
            print("\nВсе отчеты успешно созданы и сохранены в файл 'output.txt'")
            
        elif choice == "6":
            print("Выход из программы. До свидания!")
            break
            
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт от 1 до 6.")

        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
