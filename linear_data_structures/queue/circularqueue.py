class circualrqueue:
    def __init__(self, size):
        self.size = size
        self.akhil = [None] * size
        self.front = -1
        self.rare = -1
    
    def isfull(self):
        return (self.rare + 1) % self.size == self.front
    
    def isempty(self):
        return self.front == -1

    def into(self, value):
        if self.isfull():
            print("the queue is full")
            return
        if self.isempty():
            self.front = 0
        self.akhil.append(value)
        self.rare = (self.rare + 1) % self.size
        self.akhil[self.rare] = value

    def outto(self):
        if self.isempty():
            print("queue is empty")
            return
        popped = self.akhil[self.front]
        if self.front == self.rare:
            self.front = self.rare = -1
        else:
            self.front = (self.front + 1) % self.size
        return popped
    
    def display(self):
        for i in range(self.size):
            print(self.akhil[i], end =" ")

auto = circualrqueue(5)
auto.into(12)
auto.into(13)
auto.into(15)
auto.into(16)
auto.into(18)
auto.outto()
auto.into(11)
auto.display()