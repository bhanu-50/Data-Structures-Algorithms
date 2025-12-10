#Remove nth node from the end of a linked list


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
        
        
    def remove_node_from_the_end(self,n):
        slow = self.head
        fast = self.head
        
        for _ in range(n):
            fast = fast.next
            
            
        while fast.next:
            
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
            
        
        
         

