import random
def bubblesort(array):
    for j in range(len(array)):# то сколько нужно сделать проходок по циклу, что-бы отсортировать
        for i in range(len(array)-1): # проход по элементам массива и их проверка
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i] # меняем элементы местами, если i больше следующий
    return array


if __name__ == '__main__':
    arr = [random.randint(-10,100) for i in range(0,11) ] # генерация случайного списка
    print(f"non-sorted array - \n {arr}")
    print(f"sorted array - \n {bubblesort(arr)}")