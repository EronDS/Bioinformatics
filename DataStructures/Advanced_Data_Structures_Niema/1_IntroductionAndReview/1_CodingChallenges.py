
def addNums(n:int) -> int: # O(n)
    '''Return summation of 0 to n elements'''
    out = 0
    for i in range(n+1):
        out+=i
    return out

def createVector(n:int) -> list:
    '''Create vector with elements of 0 to n'''
    vec = [] 
    for i in range(1,n+1):
        vec.append(i)
    return vec

import random
def flipCoin():
    ''' Fliping unbiased coin'''
    coin = [0,1]
    return random.choice(coin)
flipCoin()

def rollDie(k:int) -> int:
    ''' Rolling k-sided dice '''
    k_sided = [i for i in range(1,k+1)] 
    return random.choice(k_sided)
rollDie(6)

def flipCoin(p:float=.5) -> bool:
    ''' Simmulation of biased coin'''
    if random.random() <= p:
        return 1
    return 0
flipCoin(.7)

def distinctSymbols(bytes:int) -> int:
    n = 8 * bytes
    return 2**n
distinctSymbols(4)
## represent binary as 0b ... where ... = binary number

def binarytoDecimal(binary_value:int) -> int:
    return int(str(binary_value),2)

def binarySum(a:str,b:str) -> int:
    """ Summation of two binary values"""
    sum_ = bin(int(a, 2) + (int(b, 2)))
    return sum[2:]
binarySum('101','101')
