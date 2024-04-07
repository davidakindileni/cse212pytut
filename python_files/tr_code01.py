class BST:
    """
    This BST class will implement our tree structure and house
    all the necessary functions. - tr_code01.py
    """
    class Node:

        # creates a class Node for each node in the tree with a left and right pointer.
        def __init__(self, data):
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        # Initialize an empty BST.
        self.root = None
