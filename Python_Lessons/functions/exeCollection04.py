'''
OrderedDict - Similar to Dictionary 
Insertion Order is better in the OrderedDict as compared to Dictionary.
It handle the rendering of the elements better than the dictionary.
'''
from collections import OrderedDict
import sys

def playWithOrderDict():
    od1 = OrderedDict()
    od1['Ravi'] = 'IT'
    od1['Surya'] = 'CSE'
    od1['Kiran'] = 'IT'
    print(od1)
    print(sorted(od1))
    for i in od1.keys():
        print(i)
    for i in od1.values():
        print(i)
    #items key/value pairs
    for k,v in od1.items():
        print(f'key is {k} , value is {v}')

    print(od1)
    # move_to_end moves the element to the end
    od1.move_to_end('Surya') 
    print(od1)      
    item1 = od1.popitem()
    print(item1)      

if __name__ == '__main__':
    print('Value 1 from the command line' ,sys.argv[1])
    print('Value 2 from the command line' ,sys.argv[2])
    playWithOrderDict()
    