import math


def distance(arr_point):
    
    calculated_val = math.sqrt(arr_point[0]**2 + arr_point[1]**2)
            
    return calculated_val     
            


def quicksort(sequence):
    length = len(sequence)
    
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if distance(item) > distance(pivot):
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)


if __name__ == "__main__":
    arr = [[10,1],[4,5],[5,6],[8,9]]
    print(quicksort(arr))