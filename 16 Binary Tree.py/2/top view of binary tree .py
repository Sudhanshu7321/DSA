from collections import deque, defaultdict

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    
    def buildTree(self, Nodes):
        self.idx = 0
        
        def helper():
            if self.idx >= len(Nodes) or Nodes[self.idx] == -1:
                self.idx += 1
                return None
            
            NewNode = Node(Nodes[self.idx])
            self.idx += 1
            NewNode.left = helper()
            NewNode.right = helper()
            return NewNode
        
        self.idx = 0
        return helper()
    
    def printTree(self, node):
        if node is None:
            return
        print(node.data, end=' ')
        self.printTree(node.left)
        self.printTree(node.right)
    
    def topView(self, root):
        if not root:
            return
        
        # Dictionary to store the top view nodes
        top_view = {}
        
        # Queue to store nodes along with their horizontal distance
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            # If a node at this horizontal distance is not present in the dictionary
            if hd not in top_view:
                top_view[hd] = node.data
            
            # Add the left and right children of the current node to the queue
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Extracting the top view nodes in order of their horizontal distance
        for key in sorted(top_view):
            print(top_view[key], end=' ')
        
    def sumOfNode(self,root):
        if not root:
            return 0
        
        q = []
        q.append(root)
        sum = 0
        
        while q:   
           currentNode = q.pop(0)
           if currentNode != None: 
                sum +=  currentNode.data
                print(currentNode.data)
                if currentNode.left != None:
                    q.append(currentNode.left)
                if currentNode.right != None:
                    q.append(currentNode.right)
                    
        print(f'Sum of node : {sum}')   
    
    def levelPrint(self,root,level):
        if not root:
            return None
        
        q = []
        l = 1
        res = []
        q.append(root)
        q.append(None)
        
        while q:
            current = q.pop(0)
            if current == None:
                l += 1
                if not q:
                    break
                else:
                    q.append(None)
            else:
                if l == level:
                    res.append(current.data)
                if current.left != None:
                    q.append(current.left)
                if current.right != None:
                    q.append(current.right)    
            
        return res
    
    def getPath(root,n,path):
        
        return
      
    def lowestCommanAnsister(self,root,n1,n2):
        path1,path2 =[]
        
        getPath(root,n1,path1)
        getPath(root,n2,path2)
        
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                return path1[i-1]
            i += 1
                         
# Test the code
Nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
bt = BinaryTree()
root = bt.buildTree(Nodes)
print("Top view of the binary tree is: ")
# bt.topView(root)
bt.sumOfNode(root)
print(bt.levelPrint(root,2))


print(bt.lowestCommanAnsister(root,n1,n2))
