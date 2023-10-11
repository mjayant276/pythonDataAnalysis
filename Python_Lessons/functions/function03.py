
'''
Factorial computation
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        result = n * factorial(n-1)
        return result

# factorial(5) -> 5 * factorial(4) -> 5 * 4 * factorial(3)

#5 * 4 * 3 * factorial(2) 
if __name__ == '__main__':
    print(factorial(5))        