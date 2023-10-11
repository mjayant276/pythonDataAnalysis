'''
deque - Doubly Linked Queue 
2. It is linear data structure
3. Perform operations on both of this linear structure
                         -------------------
(Insertion/Deletion)---> |   |    |    |    | <---- (Insertion/Deletion) 
                         -------------------
    deque can be used as queue and stack
'''
from collections import deque

def playWithDeq():
    d1 = deque()
    # append adds the elements at the end
    d1.append('Abhay')
    d1.append('Akhil')
    d1.append('Ashutosh')
    d1.append('Bimal')
    d1.append('Chirag')
    #print(d1) 
    return d1

def incrDeque(deq,ele):
    deq.extend([ele])
    return deq

def insertAtIndex(deq,index,ele):
    deq.insert(index,ele)

if __name__ == '__main__':
    d2 = playWithDeq()
    #print(d2)
    print(incrDeque(d2,'Daman'))
    # appendleft - beginning
    d2.appendleft('Bhanu')
    # print(d2)
    # print(d2[2])
    insertAtIndex(d2,4,'Chandana')
    insertAtIndex(d2,5,'Mayank')
    print(d2)
    ## remove elements
    ele1 = d2.pop()
    print(ele1)
    ele2 = d2.popleft()
    print(ele2)
    print('Remaining elements in d2' , d2)
    # remove an element using the name
    d2.remove('Ashutosh')
    print('After removing the element' , d2)