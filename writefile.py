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

