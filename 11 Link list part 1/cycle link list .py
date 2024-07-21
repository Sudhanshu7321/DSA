class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def create_cycle(self, pos):
        if pos < 0:
            return
        cycle_start = None
        temp = self.head
        count = 0
        while temp.next:
            if count == pos:
                cycle_start = temp
            temp = temp.next
            count += 1
        if cycle_start:
            temp.next = cycle_start

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def print_list(self):
        temp = self.head
        visited = set()
        while temp:
            if temp in visited:
                print(f"(cycle starts at {temp.data})", end=" -> ")
                break
            print(temp.data, end=" -> ")
            visited.add(temp)
            temp = temp.next
        print("None")

    def isCycle(self):
        slow =self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def removeCycle(self):
        slow = self.head
        fast = self.head
        
        # find cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow =self.head
                break
        
        # remove cycle
        pre = None
        while fast and fast.next:
            slow = slow.next
            pre = fast
            fast = fast.next
            if slow == fast:
                pre.next = None
                break
    def intersection(node1,node2):
        cur1 = node1
        cur2 = node2
        count1, count2 = 0, 0
        while cur1:
            cur1 = cur1.next
            count1 += 1
            
        while cur2:
            cur2 = cur2.next
            count2 += 1
         
        if count1 >= count2:
            dis = count1-count2
            cur1 = node1
            for i in range(1,dis):
                cur1 = cur1.next
        else:
            dis = count2-count1
            cur2 = node2
            for i in range(1,dis):
                cur2 = cur2.next
                
        while cur2:
            if cur1== cur2:
                return cur1.data
            cur1 = cur1.next
            cur2 = cur2.next      
        return False      
                    
                            
                        
                        
# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

# Create a cycle where the last node points to the node at position 2 (0-based index)
ll.create_cycle(2)

# Detect the cycle
print("Cycle detected:" if ll.detect_cycle() else "No cycle detected")

# Print the list (the print will show the cycle starting point for demonstration purposes)
ll.print_list()


print(f'The link list has CYCLE {ll.isCycle()}')
ll.removeCycle()
print(f'The link list has CYCLE {ll.isCycle()}')




# Intersection of Two Linked Lists


    