'''
Find the sum of all multiples of 3 or 5 below a given input.
If the given input is -ve then it should return zero.
'''

def div3r5(number):
    if number < 0:
        return 0
    return sum([num for num in range(number) if (num %3 == 0 or num %5 ==0)] )

'''
If a camel case word is present then add space in between
helloWorld -> hello World
camelCase -> camel Case
'''
def brCamelCase(s):
    return ''.join([' ' + i if i.isupper() else i for i in s])

'''
Write a function that takes a list and moves all the zeros to the end 
preservnig the order of the other elements.
'''
def moveZeros(lst):
    for num in lst:
        if 0 == num:
            lst.remove(num)
            lst.append(0)
    return lst        

#[1,2,0,1,0,1,1,0,0] -> [1,2,1,1,1,0,0,0]


if __name__ == '__main__':
    # print('Sum of numbers less than 20 ', div3r5(20))
    # assert div3r5(10) == 23
    # assert div3r5(20) == 78
    # assert div3r5(-5) == 0
    #print(brCamelCase('helloWorld'))
    #assert brCamelCase('helloWorld') == 'hello World'
    #assert brCamelCase('camelCase')  == 'camel Case'
    assert moveZeros([1,2,0,1,0,1,0,3,0,1]) == [1,2,1,1,3,1,0,0,0,0]
    assert moveZeros([1,0,1,0]) == [1,1,0,0]