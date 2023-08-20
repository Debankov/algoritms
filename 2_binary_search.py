def binary_search(array, item):
    left_border = 0 # Левая граница массива
    right_border = len(array) # Правая граница массива

    while left_border <= right_border: # ищем элемент пока не пройдёмся по всему списку
        middle_elem_index = int((left_border+right_border)/2)
        if array[middle_elem_index] == item:
            return middle_elem_index
        if item < array[middle_elem_index]: 
            right_border = middle_elem_index - 1
        else:
            left_border = middle_elem_index + 1
    return None # если элемент не был найден, возвращаем None



def recursive_binary_search(array, item, start, end):
    middle_elem_index = int((start+end)/2)
    mid_elem = array[middle_elem_index]
    if item == array[middle_elem_index]:# базовый случай
        return middle_elem_index
    if item < array[middle_elem_index]:# рекурсивные случаи
        return recursive_binary_search(array, item, start ,middle_elem_index)
    else:
        return recursive_binary_search(array, item, middle_elem_index , len(array))

if __name__ == '__main__':
    arr = [1,3,5,7,11,12,13,15,17,21,23,40,45,66,80,88]
    print(f"Исходный массив {arr}")
    print(f"Поиск элемента без рекурсии {binary_search(arr,15)}")
    print(f"Поиск элемента рекурсией {recursive_binary_search(arr,15,0,len(arr))}")
