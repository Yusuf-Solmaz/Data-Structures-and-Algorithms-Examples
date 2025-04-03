
## Question:
## Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Answer



nums = [1,3,2,1]

def containsDuplicated(nums):
    mySet = set()
    for num in nums:
        if num in mySet:
            return True
        mySet.add(num)
    return False             
        
              

print(containsDuplicated(nums))  



"""

def  method(list):
    for i in range(len(nums)):
        for j in range(i):
            print(i,j)
            if nums[i] == nums[j]:
                return True
    return False
    
"""