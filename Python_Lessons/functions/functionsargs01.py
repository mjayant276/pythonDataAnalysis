'''
This is to be used for *args 
'''
def printDescription(*args):
    print(args)
    return ' '.join(args)

# preference first position arguments and then the keyword arguments
def printDescription1(*args,sep='-'):
    return sep.join(args)

# def printDescription2(**kwargs):
#     print(kwargs)
    

def printDescription2(id,**kwargs):
    print(kwargs)
    print(id)


if __name__ == '__main__':
    #a = printDescription('Jignesh','CompSci','IInd')
    #print(a)
    #b = printDescription1('Jignesh','CompSci','IInd')
    #print(b)
    # c = printDescription1('Jignesh','CompSci',sep=';')
    # print(c)
    #d = printDescription2(name='Jignesh',dept='CompSci')
    e = printDescription2(102,name='Jignesh')