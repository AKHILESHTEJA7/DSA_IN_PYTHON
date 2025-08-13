class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class circularlinkedlist:
    def __init__(self):
        self.head = None
    def insert(self,element):
        new_node = node(element)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
    def delete(self,value):
        current = self.head
        if self.head is None: 
            print("linked list is empty")
            return
        if self.head.data == value:
            self.head = current.next
            return
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
        if current is None:
            print("value is not found")
        prev.next = current.next
        
    def upgrade(self,old,new):
        current = self.head
        while current:
            if current.data == old:
                current.data = new
                return
            current = current.next
        print("value is not found")
    
    def display(self):
        current = self.head

        while current:
            print(current.data, end= "->")
            current = current.next
        print(None)
akhil = linkedlist()
akhil.insert(12)
akhil.insert(14)
akhil.insert(16)
akhil.insert(18)
akhil.display()
akhil.delete(14)
akhil.display()
akhil.upgrade(16,20)
akhil.display()
akhil.search(18)