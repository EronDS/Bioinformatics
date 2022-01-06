def find(arr:list,n:int) -> bool:
    for i in arr:
        if i == n:return True
    return False
arr = [int(i) for i in '5 9 4 1 0 2 3'.split(' ')]
n = 0
find(arr,n)

def BinarySearch(arr:list,n:int) -> bool:
    arr = sorted(arr)
    l,r = 0,len(arr) - 1
    while l <= r:
        m = (l+r) // 2
        if arr[m] == n: return True,m
        if arr[m] > n: r = m - 1
        if arr[m] < n: l = m + 1
    return False


class Node:
    def __init__(self,value):
        self.value = value
        self.pointer = None
node1 = Node(10)
print(node1)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def traversal(self):
        if self.head is None:
            print('Linked List is Empty!!!')
        else:
            n = self.head
            while n is not None:
                print(str(n.value) + ' -> ' +\
                    str(n.pointer)) ## print(n.value)
                n = n.pointer           
    def traversal_values(self):
        if self.head is None:
            print('Linked List is Empty!!!')
        else:
            n = self.head
            while n is not None:
                print(n.value , '->', end = " ")
                n = n.pointer
    def return_string(self):
        if self.head is None:
            print('Invalid')
        else:
            string = ''
            n = self.head
            while n is not None:
                string += str(n.value) + ' -> '
                n = n.pointer
            return string[:-4]
    def add_head(self,value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.pointer = self.head
            self.head = node
    def add_tail(self,value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail =  node
        else:
            n = self.head
            while n.pointer is not None:
                n = n.pointer
            n.pointer = node
    def add_after_node(self,value,x):
        node = Node(value)
        if self.head is None:return self.add_head(value)
        n = self.head
        while n.value != x:
            n = n.pointer      
        node.pointer = n.pointer
        n.pointer = node
    def add_before_node(self,value,x):
        node = Node(value)
        n = self.head
        if self.head is None: return self.add_head(value)
        while n.pointer.value != x:
            n = n.pointer
        node.pointer = n.pointer
        n.pointer = node
    def remove_head(self):
        if self.head is None:
            print("Removal operation can't be proceed\
                 linked list is empty")
            return
        self.head = self.head.pointer
    def remove_tail(self):
        if self.head is None:
            print("Removal operation can't be proceed\
                 linked list is empty")
            return
        n = self.head
        while n.pointer.pointer is not None:
            n = n.pointer
        n.pointer = None
    def remove_x(self,x):
        if self.head is None: 
            print("Removal operation can't be proceed\
                Linked List is empty")
            return
        n = self.head
        while n.pointer.value != x:
            n = n.pointer
        n.pointer = n.pointer.pointer
    def find(self,x):
        n = self.head
        try:
            while n.value != x:
                n = n.pointer
        except: return False
        return n.value == x
    def add_from_array(self,arr):
        for i in range(len(arr)):
            self.add_after_node(arr[i], arr[i-1])
    
ll1 = LinkedList()
ll1.add_head(10)
ll1.add_tail(100)
ll1.add_head(20)
ll1.traversal()
ll1.traversal_values()
ll1.return_string()
ll1.add_after_node(6,20)
ll1.add_before_node(12,6)
ll1.remove_head()
ll1.remove_tail()
ll1.remove_x(10)
ll1.add_from_array([1,2,3])
