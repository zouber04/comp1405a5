#########################
# Author: Zouber Ismail
# Assignment 5
# Date july 11 2022
#########################


import math


def distance(arr_point):
    """
    Calculates euclidean distance
    Args: 
        -array, point
    Returns: int, euclidean distance

    """
    
    calculated_val = math.sqrt(arr_point[0]**2 + arr_point[1]**2)
            
    return calculated_val     
            


def quicksort(sequence):
    """
    Sort array of points based off euclidean distance from ascending order
    Args: 
        -array, unsorted points
    Returns: array, Sorted points

    """
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
    