class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def insert(self, key):
        if key < self.key: #if left
            if self.left is None: #if left is leaf
                self.left = node(key)
            else:
                self.left.insert(key)
        else: #if right
            if self.right is None: #no child on right
                self.right = node(key) #make key inserted value to key there
            else:
                self.right.insert(key) #insert

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal() #traverse left func
        print(self.key) #note print is here after we go left
        if self.right:
            self.right.inorder_traversal() #traverse right func

    def preorder_traversal(self):
        print(self.key) #notice print is here
        if self.left:
            self.left.preorder_traversal() #traverse left
        if self.right:
            self.right.preorder_traversal() #traverse right

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal() #traverse left
        if self.right:
            self.right.postorder_traversal() #traverse right
        print(self.key) #notice it is here after going all the way right

    def search(self, key):
        if key < self.key:
            if self.key is None: #if node not there then false
                return False
            else:
                return self.left.search(key) #search left side tree if node exists
        elif key > self.key: #if key bigger than parent go right
            if self.right is None:
                return False #if no node on right side
            else:
                return self.right.search(key) #search right
        else:
            return True #key is found = true

    def delete(self, key):
        if self is None: #checking if node contains a key
            return self
        if key < self.key: #if left
            self.left = self.left.delete(key)
        elif key > self.key: # if right
            self.right = self.right.delete(key) #deletion passed down to the right of the right
        else:
            if not self.left and not self.right: #if not children
                return None
            if not self.left: #if child is on right
                return self.right
            if not self.right: #if child is on left
                return self.left
            successor = self.right #go through right side of tree
            while successor.left: #find smallest so go left iteration
                successor = successor.left #update succ to left for following code here
            self.key = successor.key #updates the key to parent node
            self.right = self.right.delete(successor.key) #deleted previous child node
        return self #outputs updated new node


tree = node(10) #the head node/parent of all parents
tree.insert(5) #inserting all the values for the tree/real world implementation
tree.insert(2)
tree.insert(34)
tree.insert(1)
tree.insert(76)
tree.insert(7)
tree.insert(88)
tree.insert(51)
tree.insert(62)
tree.insert(1)
tree.insert(87)
tree.insert(85)
tree.insert(8)
tree.insert(13)
tree.insert(17)
tree.insert(67)
tree.insert(94)

print("-----------------")
print("Initial Node is: ", tree.key)
print("-----------------")

print("Inorder Traversal: ")
tree.inorder_traversal()
print("-----------------")
print("Preorder Traversal: ")
tree.preorder_traversal()
print("-----------------")
print("Post Order Traversal: ")
tree.postorder_traversal()
print("-----------------")
print("Search Feature: ")
#search feature below. true = exist, false = no existence
print(tree.search(5))
print(tree.search(98))
#delete feature below, deleting the previously inserted 5 value. True before, now false
print("-----------------")
print("Delete Feature: ")
tree.delete(5)
print(tree.search(5))
print("-----------------")
