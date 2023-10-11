'''
A module is a python file containing statements and definitions
Name of the module - computenumbers.py
A module can be imported into some other modules 
'''

def sumN(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

def productN(num):
    prod = 1
    for i in range(1,num+1):
        prod *= i
    return prod    
    