class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        self.freq = 0
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def add(self,word):
        node = self.root
        
        for c in word:
            
            if c not in node.children:
                node.children[c] = Node()
            node.freq += 1
            node = node.children[c]     
        node.end = True    
        
    def prefix(self,words):
        
        res = []
        for word in words:
            st = ''
            node = self.root

            for c in word:
                if c in node.children:
                    st += c
                    node = node.children[c]
                    if node.freq == 1 or node.end:
                        res.append(st)  
                        break
        print(res)          
    
    def count(self,word):
        node = self.root
        for c in word:
            if c in node.children:
                print(node.freq,end="")
                node = node.children[c] 
        print("")                   
        
t = Trie()

words = ['zebra','dog','dUCK','dove']
for word in words:
    t.add(word)
    
t.prefix(words)
            
               
                            