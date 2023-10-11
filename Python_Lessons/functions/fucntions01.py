'''
This is an exmaple on functions - can be used to call
'''
# factorial 10!
# 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
# 1 * 2 * 3 * 4 * .......  * n

def iterativeFactorial(n):
    result = 1
    for i in range(2,n+1):
        result = i * result # 2*1 # 2 *3 # 
    return result    




if __name__ == '__main__':
    print(iterativeFactorial(5))