'''
This file introduces to collections. 
- namedtuple -  (tuple)
- Counter - ( Dictionary)
- OrderedDict - (Dictionary)
- deque  - (stack and queue) LIFO, FIFO 
           (Doubly ended queue)
'''
## Collections is module in python standad library - 
#import collections
#st2 = collections.namedtuple

# second options importng the collection object 
from collections import namedtuple



# What is a namedtuple
# namedtuple is a tuple that is available in the collections module
# it is alternative to tuple
# named fileds can be created with namedtuple
# Access fields using the names instead of index

def playWithNT():
    Student = namedtuple('Student','name,age,department,year')
    st1 = Student('Rajesh',19,'CSE','IInd')
    print(type(st1))
    print(st1)
    print('Age of the student st1 --> ', st1.age)
    name,age,dept,yr = st1
    print(f'Name is {name} age is {age} , dept is {dept}, year is yr {yr}')
    print('Name is {} age is {} , dept is {}, year is yr {}'.format(name,age,dept,yr))
    # _replace on namedtuple (st1)
    st1 = st1._replace(name='Rajesh Khanna')
    name,age,dept,yr  = st1
    print('Modified Name is {} age is {} , dept is {}, year is yr {}'.format(name,age,dept,yr))
    # access the values based on index
    print(' access Name is {} age is {} , dept is {}, year is yr {}'.format(st1[0],st1[1],st1[2],st1[3]))
    
    # _make() - we pass list of values to the make function on the namedTuple
    data = ['Kailash',18,'Humanities','Ist']
    st2 = Student._make(data)
    print('New student - ', st2)

    # _asdict() --> present the namedtuple as dictionary.
    print('Named Tuple as dictionary ', st2._asdict())

    # _fields are there 
    print('Named Tuple fieds , ', st2._fields)


if __name__ == '__main__':
    playWithNT()