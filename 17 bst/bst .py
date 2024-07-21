class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
class BinaryTree:
        
    @staticmethod
    def create(root, val):
        
        def helper(root, val):
            if root is None:
                return Node(val)
                
            if root.data > val:
                root.left = helper(root.left, val)
            else:
                root.right = helper(root.right, val)    
                
            return root   
        
        return helper(root, val)    

values = [5, 1, 3, 4, 2, 7]
bt = BinaryTree()
root = None

for val in values:
    root = bt.create(root, val)  # Update root with the result of bt.create

# Function to print tree in inorder fashion to verify
def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)

inorder_traversal(root)  # Should print the nodes in sorted orde