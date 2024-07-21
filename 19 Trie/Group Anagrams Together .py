class Node:
    def __init__(self):
        self.children = {}
        self.word = []
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def add(self,word):
        node = self.root
        
        for c in sorted(word):
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.word.append(word)
        
    def collectAnagrams(self, node=None):
        if node is None:
            node = self.root
        res = []
        if node.word:
            res.append(node.word)
        for child in node.children.values():
            res.extend(self.collectAnagrams(child))
        return res  
    
    def collect_anagrams1(self, node=None):
        if node is None:
            node = self.root
        result = []
        if node.words:
            result.append(node.words)
        for child in node.children.values():
            child_result = self.collect_anagrams(child)
            for item in child_result:
                result.append(item)
        return result  
        
        
        
strs = ["eat","tea","tan","ate","nat","bat"]  
t = Trie()
for word in strs:
    t.add(word)

print(t.collectAnagrams())    
                              