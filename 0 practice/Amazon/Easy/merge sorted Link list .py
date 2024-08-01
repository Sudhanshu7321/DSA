class Node:
    def __init__(self,d):
        self.d = d
        self.n = None
        
class LinkList:
    
    def __init__(self):
        self.head = None
          
    def add(self,d):
        node = self.head
        if not node:
            self.head = Node(d)
        else: 
            while node.n:
                node = node.n
            node.n = Node(d)

    def mergeLinkList(self,head1, head2):
        
        if not head1:
            return head2
        if not head2:
            return head1
        curr1  = head1
        curr2  = head2
        
        head = None
        while curr1 and curr2:
            
            
            if curr1.d <= curr2.d:
                if not head:
                    head = curr1
                else:    
                    node = head    
                    while node.n:
                        node = node.n
                    node.n = curr1
                    curr1 = curr1.n   
            else:
                
                if not head:
                    head = curr2
                else:    
                    node = head    
                    while node.n:
                        node = node.n
                    node.n = curr2
                    curr2 = curr2.n            
        
        return head        
        
    def display(self):
        node = self.head
        while node:
            print(node.d,end=',')
            node = node.n
l1 = LinkList()
l2 = LinkList()

nodes1 = [1,2,4]
nodes2 = [1,3,4]

for node in nodes1:
    l1.add(node) 
      
for node in nodes2:
    l2.add(node)   

ml = LinkList()
ml.mergeLinkList(l1,l2)

ml.display()                 
# l2.display()                 
                        
        