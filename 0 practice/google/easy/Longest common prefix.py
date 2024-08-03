class Node:
    def __init__(self,w):
        self.child = {}
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = {}
        
    def add(self,word):
        node = self.root
        
        for c in word:
            if c not in node.child:
                node.child[c] = Node()
            node = node.child[c] 
               
        node.end = True        

strs = ["flower","flow","flight"]
t = Trie()
for word in strs:

    t.add(word)
# Output: "fl"