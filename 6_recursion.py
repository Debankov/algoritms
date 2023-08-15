# задачи с факториалами
def factorial(num): # решение задачи с факториалом без рекурсии
    result = 1
    for i in range(1,num+1):
        result *=  i
    return result

def RecFactorial(num):
    if num == 1:
        return 1
    return num * RecFactorial(num-1)

# Задачи с числами фибоначи

def fibonachi(num): # num - количество элементов в выходном массиве
    result = [0,1]
    for i in range(1,num-1):
        result.append(result[i-1]+result[i])
    return result # возвращает массив с числами фибоначи

def RecFibonachi(num): # num - индекс числа из чисел фибоначи
    if num == 1 or num == 2: # базовый случай
        return 1
    return RecFibonachi(num-1) + RecFibonachi(num-2) # рекурсивный случай. Возвращает число фибоначи

def RecFibocanhiToArray(num): # num - количество элементов в выходном массиве
    result = [0]
    for i in range(1,num):
        result.append(RecFibonachi(i)) # вызов рекусивной функции
    return result





if __name__ == '__main__':
    print(f"Решение факториала через for - {factorial(10)}")
    print(f"Решение фактоиала через рекурсию - {RecFactorial(10)}")
    print(f"Решение фибоначи через for - {fibonachi(20)}")
    print(f"Вывод пятого числа из чисел фибоначи - {RecFibonachi(5)}")
    print(f"Решение фибоначи через рекурсию - {RecFibocanhiToArray(20)}")

