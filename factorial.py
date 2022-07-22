#########################
# Author: Zouber Ismail
# Assignment 3 
# Date july 11 2022
#########################
from collections import defaultdict

def calculate(n):
    
    if n == 1:
          
        return n  
    else:  
        
        recur = n*calculate(n-1)
        
        return recur


def cachedfactorial(num,cached_dict):
    fact_num = int(num)
    result = calculate(fact_num)
    
    cached_dict[num] = result
    
    return
   


if __name__ == "__main__":
    numdict = {}
    num = cachedfactorial('5',numdict)
    print(numdict)