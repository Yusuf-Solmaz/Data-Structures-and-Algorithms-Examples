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