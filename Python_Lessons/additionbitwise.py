def addusingBitwiseOperator(x,y):
    while (y != 0):
        
        carry = x & y
        x = x^y
        y = x << 1    
    return x    
        
