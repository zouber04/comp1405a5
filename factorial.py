#########################
# Author: Zouber Ismail
# Assignment 3 
# Date july 11 2022
#########################
from collections import defaultdict

def calculate(n,cached_dict):
    
    if n == 1:
          
        return n  
    else:  
        
        recur = n*calculate(n-1,cached_dict)
        cached_dict[n] = recur
        
        return recur


def cachedfactorial(num,cached_dict):
    if num in cached_dict:
        return cached_dict[num]

    result = calculate(num,cached_dict)
    
    cached_dict[num] = result
    
    return result
   


if __name__ == "__main__":
    numdict = {}
    num = cachedfactorial(5,numdict)
    num2 = cachedfactorial(6,numdict)
    num3 = cachedfactorial(3,numdict)
    print(num3)