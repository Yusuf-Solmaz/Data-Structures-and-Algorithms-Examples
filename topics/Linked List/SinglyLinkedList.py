class Node():

    def __init__(self,value):
        self.value = value
        self.next = None
        

firstNode = Node(1)
secondNode = Node(2)
thirdNode = Node(3)

firstNode.next = secondNode
secondNode.next = thirdNode


print(firstNode.value)
print(firstNode.next.value)
print(firstNode.next.next.value)   