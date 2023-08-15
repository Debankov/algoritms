import random

def quick_sort(array):
    pass


if __name__ == '__main__':
    arr = [random.randint(-10,100) for i in range(0,11) ] # генерация случайного списка
    print(f"non-sorted array - \n {arr}")
    print(f"sorted array - \n {quick_sort(arr)}")
