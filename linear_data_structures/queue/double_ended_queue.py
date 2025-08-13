class dequeue:
    def __init__(self):
        self.cake = []
    
    def isempty(self):
        return len(self.cake) == 0
    
    def plus(self,value):
        self.cake.append(value)
    
    def plusleft(self,value):
        self.cake.insert(0,value)
    
    def minus(self):
        if self.isempty():
            return "queue is empty"
        self.cake.pop()
    
    def minusleft(self):
        if self.isempty():
            return "queue is empty"
        self.cake.pop(0)

    def display(self):
        print(self.cake)

akhil = dequeue()
akhil.plus(12)
akhil.plus(13)
akhil.plus(14)
akhil.plusleft(11)
print("this is plus: ",akhil.cake)
akhil.minus()
print("this is minus: ",akhil.cake)
akhil.minusleft()
print("this is minusleft: ",akhil.cake)
