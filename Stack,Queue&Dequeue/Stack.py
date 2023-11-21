class Stack():
    def __init__(self):
        self.elements=[]
        
    def isEmpty(self):
        return self.elements == []
    
    def push(self,value):
        self.elements.append(value)
        
    def pop (self):
        self.elements.pop()

    def showLast(self):
        return self.elements[-1]

class Test():
    
    myStack = Stack()
    myStack.push(1)
    myStack.push(2)  
    myStack.pop()         
    print(myStack.isEmpty()) 
    print(myStack.showLast())
    
    myStack.pop()
    print(myStack.elements)