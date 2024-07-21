class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end = True
        
    def search(self,word):
        node =self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.end   
    
    def startWith(self,prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
        
t = Trie()
t.insert('apple')
t.insert('apply')
t.insert('appreciate')
t.insert('approve')
t.insert('appointment')

print(t.startWith('app'))                 
# print(t.search('sudhanshu'))                 
                    