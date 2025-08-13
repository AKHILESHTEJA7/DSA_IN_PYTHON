class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,element):
        new_node = node(element)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def delete(self,value):
        current = self.head
        if self.head is None:
            print("linked list is empty")
            return
        if self.head == value:
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
    def search(self,value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                print(f"index of this {value} is :", index)
            index += 1
            current = current.next
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