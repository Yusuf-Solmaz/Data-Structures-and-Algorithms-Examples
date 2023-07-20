
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

