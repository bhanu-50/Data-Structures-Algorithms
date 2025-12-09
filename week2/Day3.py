#Find the middle element of a linked list in one pass.

#class for linked list
class SLL:
    
    class node:
        def __init__(self,data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = None
        
        
    def insert_node(self,data):
        new_node = self.node(data)
        if self.head == None:
            self.head = new_node
            return None
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def delete_node(self,key):
        temp = self.head
        
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return None
        
        prv = None
        while temp and temp.data != key:
            prv = temp
            temp = temp.next
            
        if not temp:
            return "No such element found"
        
        prv.next = temp.next
        temp = None
    
    def display(self):
        temp = self.head
        elements = []
        
        while temp:
            elements.append(temp.data)
            temp = temp.next
        
        print(f'Linked List : {elements}')
    
    
    
    
    
    #solution for the given problem
    def mid_ele(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            
            
        return slow.data
        


l = SLL()
for i in range(1,10):
    l.insert_node(i)
l.display()

print(l.mid_ele())
