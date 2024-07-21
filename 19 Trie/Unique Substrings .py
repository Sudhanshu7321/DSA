class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
               
    def suffix(self, s):
        suff = []
        for i in range(len(s)):
            suff.append(s[i:])
        return suff 
    
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end = True  
    
    def countNodes(self, node):
        if not node:
            return 0
        count = 1  # Count the current node
        for child in node.children.values():
            count += self.countNodes(child)
        return count
            
s = 'ababa'

t = Trie()

# Step 1: Generate suffixes
suff = t.suffix(s)

# Step 2: Add each suffix to the Trie
for word in suff:
    t.add(word)
    
# Step 3: Count the nodes in the Trie
ans = t.countNodes(t.root)

print(f'The total unique Substrings are: {ans}')
