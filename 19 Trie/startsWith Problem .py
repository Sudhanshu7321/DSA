class Node:
    def __init__(self):
        self.children = {}
        self.end =False
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def add(self,word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end = True            
        
    def startWith(self,word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
            
        return True                
    
t = Trie()

words = ['apple','app','mango','man','woman']
pre = 'man'
for word in words:
    t.add(word)
    
print(t.startWith(pre))        