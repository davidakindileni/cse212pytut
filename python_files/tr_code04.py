    # tr_code04.py
    def get_height(self):
        # If the tree is empty, then return 0.  Otherwise, call 
        # _get_height on the root which will recursively determine the 
        # height of the tree.
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Begin at the root

    def _get_height(self, node):
        # This function is called by the get_height function

        if node.left and node.right:
            return 1 + max(self._get_height(node.left), self._get_height(node.right))
        elif node.left:
            return 1 + self._get_height(node.left)
        elif node.right:
            return 1 + self._get_height(node.right)
        else:
            return 1

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

print(myTree.get_height())
myTree.insert(6)
print(myTree.get_height())
myTree.insert(112)
print(myTree.get_height())
