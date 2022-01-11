class BST: 
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
    def insert(self,value):
        if self.value is None:
            self.value = value
            return 
        if value == self.value:return
        if value < self.value:
            if self.left != None:
                self.left.insert(value)
            else:
                self.left = BST(value)
        if value > self.value:
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = BST(value)
    def insert_from_array(self,arr):
        for i in arr:
            self.insert(i)
    def search(self,value):
        if self.value == value:
            print('True')
            return
        if value < self.value:
            if self.left == None:
                print('False')
                return
            self.left.search(value)
        else:
            if self.right == None:
                print('False')
                return
            self.right.search(value)
    def VLR_traversal(self):
        ''' Pre-Order Traversal '''
        print(self.value)
        if self.left:
            self.left.VLR_traversal()
        if self.right:
            self.right.VLR_traversal()
    def LVR_traversal(self):
        ''' In-order Traversal '''
        if self.left:
            self.left.LVR_traversal()
        print(self.value)
        if self.right:
            self.right.LVR_traversal()
    def LRV_traversal(self):
        ''' Post-Order Traversal '''
        if self.left:
            self.left.LVR_traversal()
        if self.right:
            self.right.LVR_traversal()
        print(self.value)
    def min(self):
        node = self
        while node.left:
            node = node.left
        return node.value
    def max(self):
        node = self
        while node.right:
            node = node.right
        return node.value


bst = BST(10)
bst.insert(20)
bst.insert(15)
bst.insert(21)
bst.search(11)
bst.insert(8)
bst.insert(9)
bst.insert(7)
bst.VLR_traversal()
bst.LRV_traversal()
bst.LRV_traversal()
bst.min()
bst.max()