def sortList(head):
    
    def middleNode(node):
        slow, fast = node, node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        sl = slow.next    
        slow.next = None            
        return sl   
        
    def mergeTwoList(list1, list2): 
        head = NodeList()
        dummy = head
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next    
            head = head.next   
        
        if  list1:
            head.next = list1
               
            
        if list2:
            head.next = list2
            
        return dummy.next    
                            
    if not head or head.next == None:
        return head
    
    mid = middleNode(head)
    left = sortList(head)
    right = sortList(mid)
    return mergeTwoList(left,right)