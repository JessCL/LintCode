# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/longest-increasing-subsequence
@Language: Python
@Datetime: 16-12-10 00:00
'''

class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [1 for _ in range(n)]
        
        for i in range(n):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        result = 1          
        for i in range(n):
            if dp[i] > result:
                result = dp[i]
        
        return result