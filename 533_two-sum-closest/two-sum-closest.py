# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/two-sum-closest
@Language: Python
@Datetime: 16-12-21 02:16
'''

class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumCloset(self, nums, target):
        for i in range(len(nums)):
            nums[i] = (nums[i], i)
        nums.sort()
        start = 0
        end = len(nums) - 1
        diff = sys.maxint
        while start < end:
            if nums[start][0] + nums[end][0] == target:
                return 0
            else:
                if abs(nums[start][0] + nums[end][0] - target) < diff:
                    diff = abs(nums[start][0] + nums[end][0] - target)
                
                if nums[start][0] + nums[end][0] < target:
                    start += 1
                else:
                    end -= 1
        return diff
        
                