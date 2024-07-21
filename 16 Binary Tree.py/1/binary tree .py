class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None  

class BinaryTree:
    
    def buildTree(self, Nodes):
        self.idx = 0  # Use a simple variable to keep track of the index
        
        def helper():
            if self.idx >= len(Nodes) or Nodes[self.idx] == -1:
                self.idx += 1
                return None
            
            NewNode = Node(Nodes[self.idx])
            self.idx += 1
            NewNode.left = helper()
            NewNode.right = helper()
            return NewNode
        
        return helper()
    
    def printPreOrder(self, node):
        if node is None:
            return
        print(node.data, end=' ')
        self.printPreOrder(node.left)
        self.printPreOrder(node.right)
    
    def printInOrder(self, node):
        if node is None:
            return
        self.printInOrder(node.left)
        print(node.data, end=' ')
        self.printInOrder(node.right)
    
    def printPostOrder(self, node):
        if node is None:
            return
        self.printPostOrder(node.left)
        self.printPostOrder(node.right)
        print(node.data, end=' ')
    
    def printLavelOrder(self,root):
        if not root:
            return
        
        queue = []
        queue.append(root)
        queue.append(None)
        
        while queue:
            currentNode = queue.pop(0)
            if currentNode == None:
                print("")
                if not queue:
                    break
                else:
                    queue.append(None)
            else:
                print(currentNode.data,end='')
                if currentNode.left != None:
                    queue.append(currentNode.left)
                            
                if currentNode.right != None:
                    queue.append(currentNode.right)
     
    def heightOfTree(self,root):
        
        def helper(root):
            
            if not root:
                return 0
            
            lh = helper(root.left)
            rh = helper(root.right)
            return max(lh,rh) + 1
        
        return helper(root)                     
                    
        
        
        
        
        
Nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]        
bt = BinaryTree()
root = bt.buildTree(Nodes)  # Store the root node for further operations

print("Pre-Order")
bt.printPreOrder(root)  # Print the tree in pre-order traversal
print("In-Order")
bt.printInOrder(root)  # Print the tree in in-order traversal
print("Post-Order")
bt.printPostOrder(root)  # Print the tree in post-order traversal

bt.printLavelOrder(root)

print(f'Height of Tree : {bt.heightOfTree(root)}')