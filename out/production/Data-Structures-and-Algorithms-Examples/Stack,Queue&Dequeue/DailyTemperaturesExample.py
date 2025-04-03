'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
'''
from collections import deque

def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []  
    
    for ix, temperature in enumerate(temperatures):
        while stack and temperature > stack[-1][0]:
            stackTemperature, stackIndex = stack.pop()
            result[stackIndex] = (ix - stackIndex)
        stack.append([temperature, ix])
    return result

# Example 1:
temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperatures(temperatures1))


          