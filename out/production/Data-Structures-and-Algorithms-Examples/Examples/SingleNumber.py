# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# O(n) -> Time Complexity , O(1) -> Space Complexity

"""
Example 1:

Input: nums = [2,2,1]
Output: 1

"""

nums = [2,2,1,5,1,5,7]



def singleNumber(nums : list):
   tempNum = 0
   for num in nums:
       tempNum = tempNum ^ num
       
   return tempNum          
        

print(singleNumber(nums))            

                    

                       

                    
            
 