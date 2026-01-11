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

