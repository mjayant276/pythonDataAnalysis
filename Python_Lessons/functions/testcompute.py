'''
Import the module computenumbers and test it.
'''

#import computenumbers
# from computenumbers import sumN 
# from computenumbers import productN
#from computenumbers import *
from computenumbers import sumN,productN

if __name__ == '__main__':
    #sumn = sumN(10)
    sumn = sumN(10)
    prodN = productN(5)
    print('SUm of 10 numbers is ', sumn)
    print('Product of 5 numbers', prodN)