# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/maximum-number-in-mountain-sequence
@Language: Python
@Datetime: 16-11-22 20:48
'''

class Solution:
    # @param {int[]} nums a mountain sequence which increase firstly and then decrease
    # @return {int} then mountain top
    def mountainSequence(self, nums):
        if len(nums) == 0:
            return None
        start = 0
        end = len(nums) - 1
        while (start + 1 < end):
            mid = start + (end - start) / 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid + 1]:
                return nums[mid]
            elif nums[mid-1] <= nums[mid] and nums[mid] <= nums[mid + 1]:
                start = mid
            else:
                end = mid
        if nums[start] > nums[end]:
            return nums[start]
        else:
            return nums[end]
                