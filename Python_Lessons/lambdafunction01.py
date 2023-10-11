# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:13:13 2023

@author: Jayanth
Anonymous functions - THey dont have a name
multiple usage not there - specified functoinality
"""

def squareVal(x):
    return x**2

if __name__ == '__main__':
    # y = lambda x : x**2
    # print(y)
    # print(y(2))
    # upperCase = lambda y : y.upper()
    # print(upperCase('helllo'))
    listVal = [1,2,3,4,5]
    out = []
    for i in listVal:
        z = squareVal(i)
        out.append(z)
    print(out)    
    print(list(map(lambda x : x**2 ,listVal)))