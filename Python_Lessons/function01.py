# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 21:09:39 2023

@author: Jayanth
"""

def iterativeFactorial(n):
    result = 1
    for i in range(2,n+1):
        result = i * result # 2*1 # 2 *3 # 
    return result    




if __name__ == '__main__':
    print(iterativeFactorial(5)) 