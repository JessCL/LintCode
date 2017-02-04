# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array
@Language: Python
@Datetime: 16-11-09 07:27
'''

class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        # write your code here
        start = 0
        end = len(nums) - 1
        if len(nums) == 0:
            return 0
        while start + 1 < end:
            mid = start + (end - start) / 2
            if mid > 0  and nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid
            # mid will not equal to end
   
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]
        
        