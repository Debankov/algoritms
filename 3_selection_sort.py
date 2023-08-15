import random

def selectionSort(array):
    for i in range(len(array)):
        indexMin = i
        for j in range(i+1,len(array)):
            if array[j] < array[indexMin]:
                indexMin = j
            
        tmp = array[i] # временная переменная хранящая в себе элемент из списка
        array[i] = array[indexMin] 
        array[indexMin] = tmp # меняем переменные местами
    return array

if __name__ == '__main__':
    arr = [random.randint(-10,100) for i in range(0,11) ] # генерация случайного списка
    print(f"non-sorted array - \n {arr}")
    print(f"sorted array - \n {selectionSort(arr)}")
    # print(selectionSearch(arr))
    
 