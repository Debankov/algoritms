def binary_search(array, item):
    left_border = 0 # Левая граница массива
    right_border = len(array) # Правая граница массива

    while left_border <= right_border: # ищем элемент пока не пройдёмся по всему списку
        middle_elem_index = int((left_border+right_border)/2)
        if array[middle_elem_index] == item:
            return f"index of item - {middle_elem_index}"
        if item < array[middle_elem_index]: 
            right_border = middle_elem_index - 1
        else:
            left_border = middle_elem_index + 1
    return None # если элемент не был найден, возвращаем None


if __name__ == '__main__':
    arr = [1,3,5,7,12,11,13,15,17,21,23,40,45,66,80,88]
    print(binary_search(arr,1))
