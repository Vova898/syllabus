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

