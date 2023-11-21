class Queue():
    
    def __init__(self):
        self.elements = []
        
    def enqueue(self,value):
        self.elements.append(value)
    
    def dequeue(self):
        self.elements.pop(0)
        
    def isEmpty(self):
        return self.elements == []            
    
     
   
 
    
class Test():
    
    queue = Queue()
    
    print(queue.isEmpty())
    
    queue.enqueue(15)
    
    queue.enqueue(25)
    
    queue.enqueue(35)
    
    queue.dequeue()
    print(queue.elements)
    