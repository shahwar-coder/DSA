# https://leetcode.com/problems/running-sum-of-1d-array/description/
from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        new_nums=[]
        for index, num in enumerate(nums):
            for j in range(0,index+1):
                sum+=nums[j]
            new_nums.append(sum)
            sum=0
        return new_nums
    
obj1 = Solution()
print(obj1.runningSum([1,2,3,4,5]))