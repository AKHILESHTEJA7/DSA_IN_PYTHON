class node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class doublelinkedlist:
    def __init__(self):
        self.head = None
    
    def add(self,value):
        new_node = node(value)

        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    def remove(self,value):
        current = self.head
        if self.head is None:
            print("linked list is empyt")
            return
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
    
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    
    def display_backward(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data,end = "<->")
            current = current.prev
        print("none")

akhil = doublelinkedlist()
akhil.add(12)
akhil.add(90)
akhil.add(78)
akhil.add(15)

akhil.display_forward()
akhil.remove(90)
akhil.display_backward()