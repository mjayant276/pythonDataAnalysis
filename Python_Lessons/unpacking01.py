# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 20:52:33 2023

@author: Jayanth
"""

'''
How unpacking works in python
'''

def unpackValue():
    args = [7,14]
    return list(range(*args))

def unpackValue1():
    *x,y = 'Ravi','Kishan','Kriplani','Mahesh','Suraj'
    print(x)
    print(y)
 
def unpackValue2():
    names = ('Ravi','Kishan','Kriplani')
    name1 = 'Mahesh'
    name2 = 'Suraj'
    print(name1,*names,name2)

def findproduct(c, a=1,b=1):
    return a*b
    
if __name__=='__main__':
    #print(unpackValue())
    #print(unpackValue1())
    unpackValue2()
    numbers = {'a':3,'b':4}
    #res = findproduct()
    res = findproduct('hello',**numbers)
    print(res)