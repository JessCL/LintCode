# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/minimum-subarray
@Language: Python
@Datetime: 16-12-21 01:25
'''

class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            if dp[i-1] >= 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
            if dp[i] < result:
                result = dp[i]
        return result
        
