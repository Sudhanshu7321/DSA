class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkList:
    
    def __init__(self):
        self.head = None
        
    def addFirst(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        
    def addLast(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode    
            
    def addIndex(self,data,index):
        i = 0
        temp  = self.head
        while i < index:
            temp = temp.next        
            i += 1
            
        newNode = Node(data)
        newNode.next = temp.next
        temp.next = newNode
             
    def display(self):
        element = []
        current = self.head
        while current:
            element.append(current.data)
            current = current.next
        return element    
        
    def size(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        return count    
    
    def removeFirst(self):
        current = self.head
        if current:
            self.head = current.next
            return 'First Node Deleted'
        
        return 'Link List is already Empty'  
    
    def removeLast(self):
        
        if not self.head:
            return 'Link List is already Empty'
        
        if self.head.next == None:
            self.head = None
            return 'Last Node Deleted'

            
        current = self.head
        while current.next.next:
            current = current.next
            
        current.next = None    
        return 'Last Node Deleted'
        
    def serarch(self,key):
        current = self.head
        count = 0
        
        while current:
            if current.data == key:
                return count
            count += 1
            current = current.next
        return -1    
     
     
    def recursiveSearch(self,key):
        
        def helper(head, key):
            if not head:
                return -1
            
            if head.data == key:
                return 0
            
            idx = helper(head.next,key)
            
            if idx == -1:
                return -1
            
            return idx+1
        
        return helper(self.head,key) 
    
    
    
    def reverseLinkList(self):
        pre = None
        current = self.head
        # nex = self.head
        
        while current:
            nex = current.next
            current.next = pre
            pre = current
            current = nex
        self.head = pre     
     
    def Palindrome(self):
        # Find the mid node of LL         
        def findMid(head):
            slow = head
            fast = head
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow          
    
        # Reverse 2nd half of LL 
        def reverse(head): 
            pre = None
            curr = head
            while curr:
                nex = curr.next
                curr.next = pre
                pre = curr
                curr = nex
            return pre   
        
        firstHalfHead = self.head
        mid = findMid(self.head)
        secoundHalfHead = reverse(mid)   
        while secoundHalfHead and secoundHalfHead.next:
            if firstHalfHead.data != secoundHalfHead.data:
                return False
            firstHalfHead = firstHalfHead.next
            secoundHalfHead = secoundHalfHead.next
        return True    
                
              
                                       
ll = LinkList()
# ll.addFirst(3)        
# ll.addFirst(2)        
# ll.addFirst(1)     
# ll.addLast(2)     
# ll.addIndex(1,1)

# print(ll.display())   
# # print(f'Size of linklist : {ll.size()}')   
# # print(f'Search in  linklist : {ll.serarch(1)}')   
# # print(f'Search in  linklist : {ll.recursiveSearch(1)}')   
# # print(ll.removeFirst())   
# # print(ll.removeLast())  
# print(ll.findMid()) 
# # ll.reverseLinkList()


ll.addFirst(1)
ll.addFirst(2)
ll.addFirst(3)
ll.addFirst(2)
ll.addFirst(1)

print(ll.display())   

print(ll.Palindrome())


