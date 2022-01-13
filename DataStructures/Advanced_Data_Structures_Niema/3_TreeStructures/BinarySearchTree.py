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
    def delete(self,x):
        if self.value == None:
            print("Tree is Empty!!!\
                Delete Operation can't be proceed")
            return
        if x < self.value:
            if self.left:
                self.left = self.left.delete(x)
            else:
                print('x-value not found in tree')
        if x > self.value:
            if self.right:
                self.right = self.right.delete(x)
            else:
                print('x-value not found in tree')
        else: #self.value == x
            ## 0 child or 1 chiild
            if self.left == None:
                new = self.right
                self = None
                return new
            if self.right == None:
                new = self.left
                self = None
                return new
            ## 2 child - replace with highest from lst
            ## or lowest from right subtree
            # lst = Left Subtree, rst = right subtree
            node = self.left
            while node.right:
                node = node.right
            self.value = node.value
            self.left = node.left.delete(node.value)
            return self
        

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
bst.VLR_traversal()
bst.min()
bst.max()
bst.delete(21)
bst.count()