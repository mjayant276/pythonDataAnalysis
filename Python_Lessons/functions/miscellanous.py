'''
Yield is used in place of return - yield can return multiple values
Generator object is what it returns
We shall focus on generator/yield 
'''

#yield is used in this function
def getevennums(num):
    for i in range(num):
        if i%2 == 0:
            yield i

def getfib(n):
    a,b = 0,1 # 0,1,1,2,3,5,8,13,21
    while a < n:
        yield a
        a,b = b,a+b    


if __name__ == '__main__':
    numgen = getevennums(10) # iterable object - iteration can be performed
    print(numgen)
    # print(next(numgen))
    # print(next(numgen))
    # print(next(numgen))
    # print(next(numgen))
    # print(next(numgen))
    
    for i in numgen:
        print(i ,end=' ')
    print(list(numgen))

    fibgen = getfib(35)
    for i in fibgen:
        print(i ,end=' ')
    print(list(fibgen))