# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/maximum-subarray
@Language: Python
@Datetime: 16-12-21 01:22
'''

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        dp = [0]*len(nums)
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            if dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
            if dp[i] > result:
                result = dp[i]
        return result
        