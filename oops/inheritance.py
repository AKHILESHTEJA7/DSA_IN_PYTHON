class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    
    def printthename(self):
        print(self.firstname, self.lastname)

x = person("akhil","teja")
x.printthename()