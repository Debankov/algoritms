def linear_search(array,item):
    for i in range(len(array)):
        if array[i] == item:
            return f"index of {item} in array - {i}"
    return None
        
if __name__ == '__main__':
    arr = [1,4,6,14,15,10,53,15,52,-43,12]
print(linear_search(arr,15))