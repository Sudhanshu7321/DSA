class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    
    def __init__(self):
        self.root = Node()
        
    def insert(self,word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end =True   
        
    def wordBrake(self,key):
        node = self.root
        for c in key:
            if c not in node.children:
                return False
            node = node.children[c]
            if node.end:
                node = self.root
        
        return True   
    

    
t = Trie() 
   
words = ['i','like','sam','samsung','mobile','ice']
key = 'ilikesamsamsung'
for word in words:
    t.insert(word)
    
print(t.wordBrake(key))    
    
    
                        