    def __iter__(self):
        # This function is a generator function. It carries out a forward traversal beginning from the root
        # of BST. It is called when a for loop is performed.
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        This function performs an in-order forward traversal of the BST.
        We shall continue traveling on the left side (obtaining the smaller numbers first),
        deliver the data in the current node, and then traverse on the right side 
        (obtaining the larger numbers last) if the node we are provided (the current sub-tree) exists. 

        It uses the 'yield' it enable it support for loops.

        The value for the 'for' loop to employ can be obtained by using the 'yield' keyword.
        The logic in this method will resume where the last 'yield' returned a value when the
        'for' loop needs to receive the next value. When our generator function has to call
        another function for which a `yield} will be called, the keyword 'yield from' is utilized.
        Stated otherwise, the generator function transfers the {yield} to another function. 
        The __iter__ function calls this function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

# create a tree named myTree
myTree = BST()

# insert nodes with data
myTree.insert(6)
myTree.insert(2)
myTree.insert(10)

for x in myTree:
    print(x)
