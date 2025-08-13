class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.bottom = None
    
    def enqueue(self,value):
        new_node = node(value)
        if self.bottom is None:
            self.bottom = new_node
            return

        current = self.bottom
        while current.next:
            current = current.next
        current.next = new_node
    
    def dequeue(self):
        current = self.bottom
        pop = self.bottom.data
        self.bottom = current.next
        print(f"this value is popped out:", pop)
    
    def front(self):
        return self.bottom.data
    
    def display(self):
        current = self.bottom
        while current:
            print(current.data,end= "->")
            current = current.next
        print("null")

akhil = queue()
akhil.enqueue(123)
akhil.enqueue(456)
akhil.enqueue(789)
akhil.display()
akhil.dequeue()
akhil.display()
akhil.front()
akhil.display()