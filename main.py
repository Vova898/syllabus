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
