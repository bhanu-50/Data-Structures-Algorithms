#Reverse a linked list

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
    
    def display(self):
        temp = self.head
        elements = []
        
        while temp:
            elements.append(temp.data)
            temp = temp.next
        
        print(f'Linked List : {elements}')
    
    def reverse(self):
        if self.head == None:
            return None
        elif  self.head .next == None:
             return self.head 
    
        temp_p = None 
        cr_p = self.head 
        next_p = None
        while cr_p:
            next_p = cr_p.next
            cr_p.next = temp_p
            temp_p = cr_p
            cr_p = next_p
    
        return temp_p
        


        

l = SLL()
for i in range(1,10):
    l.insert_node(i)
l.display()
temp = l.reverse()
while temp:
    print(temp.data,end=" ")
    temp = temp.next

