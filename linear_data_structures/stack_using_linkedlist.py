class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class stack:
    def __init__(self):
        self.top = None
    
    def isempty(self):
        return self.top == None
    
    def plus(self,element):
        block = node(element)
        block.next = self.top
        self.top = block
    def minus(self):
        if self.isempty():
            print("Stack underflow")
            return
        popped = self.top.data
        self.top = self.top.next
        return popped
    def look(self):
        if self.isempty():
            print("stack is empty")
            return None
        return self.top.data
    def display(self):
        current = self.top
        while current:
            print(current.data, end= "->")
            current = current.next
        print("null")

akhil = stack()
akhil.plus(23)
akhil.plus(34)
akhil.plus(45)
akhil.display()
akhil.minus()
akhil.look()
akhil.display()