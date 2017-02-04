# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/sort-colors
@Language: Python
@Datetime: 16-12-21 22:42
'''

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        if len(nums) <= 1:
            return nums
        end = self.divide(nums, 0, len(nums) - 1, 2) 
        self.divide(nums, 0, end - 1, 1) 
        
    def divide(self, nums, start, end, k):
        while start <= end:
            while start <= end and nums[start] < k:
                start += 1
            while start <= end and nums[end] >= k:
                end -= 1
            if start <= end:
                self.swap(nums, start, end)
                start += 1
                end -= 1
        return start
        
    
        
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
            
        