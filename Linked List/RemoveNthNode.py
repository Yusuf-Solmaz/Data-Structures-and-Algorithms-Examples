'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 
Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''
class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
        
        
        
firstNode = Node(1)
secondNode = Node(2)
thirdNode = Node(3)
fourthNode = Node(4)   

firstNode.next = secondNode
secondNode.next = thirdNode

secondNode.prev = firstNode
thirdNode.prev = secondNode

thirdNode.next=fourthNode
fourthNode.prev=thirdNode  

nodeList= []

def remove (n:int,head:Node):

    while(True):
        if(head.next!=None):
            nodeList.append(head.value)
            head=head.next
        else:
            break
    count = 1
    nodeList.append(head.value)  
    nodeList.pop(-n)
    print(nodeList)
    
    for temp in nodeList:
        node = Node(temp)
        if(nodeList[count] != None):
            node.next = nodeList[count]
            count += 1
        count=1   
        if(nodeList[count] != None):
            node.prev = nodeList[count-1]
            count += 1
        print(node.value)    
    
      
remove(1,firstNode)        