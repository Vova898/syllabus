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

