'''
Recursive Example - Sum of numbers (n)
'''

# Recursive 
# base condition
def sumN(n):
    # 5
    if n == 1:
        return 1
    else:
        return sumN(n-1) + n # sumN(4) (sum(3) -> sum(2) ->  + 5 -> 

# sumN(4) + 5
# sumN(3) + 4 + 5
# sumN(2) + 3 + 4 + 5
# sumN(1) + 2 + 3 + 4 + 5
# 1 + 2 + 3 + 4 + 5 = 15


if __name__ == '__main__':
    print(sumN(15))
