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

