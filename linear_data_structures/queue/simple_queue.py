#simple queue or linear queue
class akhil:
    def __init__(self):
        self.akhil = []
    def isempty(self):
        return len(self.akhil) == 0
    def enqueue(self,element):
        return self.akhil.append(element)
    def dequeue(self):
        if self.isempty():
            return "queue is empty"
        return self.akhil.pop(0)
    def peek(self):
        if self.isempty():
            return "queue is empty"
        return self.akhil[0]
    def size(self):
        return len(self.akhil)

superman = akhil()
superman.enqueue("venus")
superman.enqueue("earth")
superman.enqueue("mars")
superman.enqueue("jupitor")

print("queue list : ", superman.akhil)
superman.dequeue()
print(superman.peek())
print(superman.isempty())
print("size is: ",superman.size())
print("queue list : ", superman.akhil)