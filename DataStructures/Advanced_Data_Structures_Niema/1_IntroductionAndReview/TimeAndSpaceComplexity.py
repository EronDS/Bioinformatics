## Analyze data structures for time and space complexity 
## strenghts and weakings 

# Data Strucuteres

### TIME COMPLEXITY 

## Time Complexity = n 
# O(n) 

def print_info(a: list) -> None:
    n = len(a)
    avg = 0.0
    for i in range(n):
        print('Element %d is %d' % (i,a[i]))
        avg += a[i]
    avg /= n 
    print('Average is %f' % avg)
    
a = [1,2,3,4,5,6,7,8,9,10,11,12]
print_info(a)

## Time Complexity = n² 
# O(n²)

def dist(a: list) -> None:
    n = len(a)
    for i in range(n-1):
        for j in range(i+1,n):
            print("%d - %d = %d" % (a[j], a[i], a[j]-a[i]))
    
dist(a)

## Time complexity = n 
## O(n) = n + n/2 + n/4 ... 
# n(1+ .5 + .25 ...) -> 2
# 2n = o(n)

def tricky(n: int) -> None:
    operations = 0
    while n > 0:
        for i in range(n):
            print("Operations: %d" % operations)
            operations += 1
        n = int(n/2)

tricky(14)

#### Options ... Different Solutions to the problem in hand
# Linear O(n) Time COmplexity
def GetMax(vec:list) -> int:
    max_ = a[0]
    for i in vec:
        if i>max_:
            max_ = i
    return max_


# Avoid Convolutions # Example with n² time complexity
def GetMaxConvoluted(vec:list) -> int:
    for i in vec:
        best = True
        for j in vec:
            if i < j:
                best = False
                break
        if best:
            return i 
        
