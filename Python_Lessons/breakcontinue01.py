# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:07:11 2023

@author: Jayanth
break statements and continue statements
"""

if __name__ == '__main__':
    friends = ['Amrit','Bahubali','Chandra','Dabesh','Hrithik','Ranver']
    for name in friends:
        if name == 'Chandra':
            print('THe is done with ', name)
            break
        print('Name is ,', name) 
    
        
    ### for and else in python
    for n in range(2,20):
        for x in range(2,n):
            if n % x == 0:
                print(n, 'equals',x, '*',n//x)
                break
        else:
            print(n,' is a prime number')
            
    ## continue
    for name in friends:
        if name == 'Chandra':
            continue
        print('Name is ,', name)         