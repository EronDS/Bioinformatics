## worst-case scenario
def find(arr:list,n:int) -> bool:
    for i in arr:
        if i == n:return True
    return False
arr = [int(i) for i in '5 9 4 1 0 2 3'.split(' ')]
n = 0
find(arr,n)

## better algorithm for search
def BinarySearch(arr:list,n:int) -> bool:
    arr = sorted(arr)
    l,r = 0,len(arr) - 1
    while l <= r:
        m = (l+r) // 2
        if arr[m] == n: return True,m
        if arr[m] > n: r = m - 1
        if arr[m] < n: l = m + 1
    return False
