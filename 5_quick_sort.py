import random

def quick_sort(array):
    if len(array) < 2: # базовый случай
        return array
    else: # рекурсивный случай
        pivot = array[0] 
        less = [i for i in array[1:] if i <= pivot] # подмассив элементов меньше чем пивот
        greater = [i for i in array[1:] if i > pivot] # подмассив элементов больше чем пивот
        return quick_sort(less) + [pivot] + quick_sort(greater)





if __name__ == '__main__':
    arr = [random.randint(-10,100) for i in range(0,11) ] # генерация случайного списка
    print(f"non-sorted array - \n {arr}")
    print(f"sorted array - \n {quick_sort(arr)}")
