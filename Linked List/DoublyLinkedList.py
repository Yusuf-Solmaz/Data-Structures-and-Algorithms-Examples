class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
        
        
        
        
firstNode = Node(1)
secondNode = Node(2)
thirdNode = Node(3)   

firstNode.next = secondNode
secondNode.next = thirdNode

secondNode.prev = firstNode
thirdNode.prev = secondNode


print(firstNode.next.next.value)   

print(thirdNode.prev.prev.value)
   