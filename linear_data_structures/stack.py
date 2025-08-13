class vishnu:
    def __init__(self):
        self.stack = []
    
    def isempty(self):
        return len(self.stack) == 0
    
    def push(self, element):
        return self.stack.append(element)
    
    def pop(self):
        if self.isempty():
            return "stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isempty():
            return "stack is empty"
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)

doreamon = vishnu()
doreamon.push("akhilesh")
doreamon.push("vishnu")
doreamon.push("mommy")
doreamon.push("daddy")
print("size of the stack: ",doreamon.size())
print("stack contains: ", doreamon.stack)
print("using pop:", doreamon.pop())
print("peek value is : ", doreamon.peek())
print("check is empty: ", doreamon.isempty())
print("stack contains: ", doreamon.stack)