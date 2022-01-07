
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def front_traversal(self):
        if self.head is None: 
            print('Linked List is Empty!!!')
            return 
        n = self.head
        while n != None:
            print(n.value, ' ->', end = ' ')
            n = n.next

    def back_traversal(self):
        if self.head is None: 
            print('Linked List is Empty!!!')
            return
        n = self.tail
        while n != None:
            print(n.value, ' ->', end=' ')
            n = n.prev
            
    def add_head(self,value):
        if self.head is None:
            self.head = self.tail = Node(value)
            return 
        node = Node(value)
        self.head.prev = node
        node.next = self.head
        self.head = node
        
    def add_tail(self,value):
        if self.head is None:
            self.head=self.tail=Node(value)
            return
        node = Node(value)
        self.tail.next = node
        node.prev = self.tail 
        self.tail = node
    
    def insert_after_node(self,value,x=None):
        if self.head is None:return self.add_head(value)
        n = self.head
        node = Node(value)
        while n.value != x and n.value != None:
            n = n.next    
        node.next = n.next
        node.prev = n
        if n.next is not None:
            n.next.prev = node
        else:
            self.tail = node
        n.next = node
        
    def insert_before_node(self,value,x=None):
        if self.head is None: return self.add_head(value)
        n = self.head
        node = Node(value)
        while n.value != x:
            n.next
        node.next = n
        node.prev = n.prev
        n.prev = node
        if n.prev is not None:
            n.prev.next = node
        else:
            self.head = node
    def remove_head(self):
        if self.head is None:
            print("Removal Operation can't be proceed\
                Linked List is Empty!!!")
            return
        if self.head.next is None:
            self.head = self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None
    def remove_tail(self):
        if self.tail is None:
            print("Removal Operation can't be proceed\
                Linked List is Empty!!!")
            return
        if self.tail.prev is None:
            self.tail = self.head = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

dll = DoublyLinkedList()
dll.add_head(10)
dll.add_tail(20)
dll.front_traversal()
dll.insert_after_node(15,10)
dll.back_traversal()
dll.insert_after_node(15,20)
dll.remove_head()
dll.remove_tail()