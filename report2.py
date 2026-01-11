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

