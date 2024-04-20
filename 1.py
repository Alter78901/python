from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        while left <= right:
            m = (left+right)//2
            if target < nums[m]:
                right = m-1
            elif target > nums[m]:
                left = m+1
            else:
                return m
        return right+1
nums = [1,3,5,6]
target = 5
print(Solution().searchInsert(nums, target))
