    # The two functions below work together to enable us to search for value inside our tree.

    def __contains__(self, data):
        # This function allows to check if a value is present in the tree

        return self._contains(data, self.root)  # Begin at the root

    def _contains(self, data, node):
        # This function is called by the __contains__ function.
        # It searches for a node that contains the "data".
        if not node:
            return False
        if node.data == data:
            return True
        if node.data > data:
            return self._contains(data, node.left)
        return self._contains(data, node.right)

# create a tree named myTree
myTree = BST()

# insert nodes with data
myTree.insert(6)
myTree.insert(2)
myTree.insert(10)
myTree.insert(19)
myTree.insert(26)
myTree.insert(4)
myTree.insert(17)
myTree.insert(10)
myTree.insert(29)

print(10 in myTree) # True
print(245 in myTree) # False
print(29 in myTree) # True
print(6 in myTree) # True
