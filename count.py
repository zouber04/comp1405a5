#########################
# Author: Zouber Ismail
# Assignment 3 
# Date july 20 2022
#########################

def countingSort(arr):
    """
    Sorting list of number in asceding order
    Args: 
        -int array, numbers
    Returns: int array, sorted numbers

    """
    
    size = len(arr)
    output = [0] * size

    # count array initialization
    count = [0]*(size+3)

    # storing the count of each element 
    for m in range(0, size):
        count[arr[m]] += 1
    print(count)
    # storing the cumulative count
    for m in range(1, 10):
        count[m] += count[m - 1]

    # place the elements in output array after finding the index of each element of original array in count array
    m = size - 1
    while m >= 0:
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1

    for m in range(0, size):
        arr[m] = output[m]
    
if __name__ == "__main__":
    data = [3,5,1,6,7,8,3]
    countingSort(data)
    print("Sorted Array: ")
    print(data)
 
    