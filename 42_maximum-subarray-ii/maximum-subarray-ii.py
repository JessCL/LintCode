# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/maximum-subarray-ii
@Language: Python
@Datetime: 16-12-21 00:40
'''

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        if len(nums) <= 1:
            return 0
 
        preSum = [0] + nums[:]
            
        preMS = [0] * len(preSum)  # åæ¬ç¬¬i-1ä¸ªåç´ 
        postMS = [0] * len(preSum) # åæ¬ç¬¬i-1ä¸ªåç´  
        curMin = sys.maxint
        maxSum = nums[0]
        for i in range(len(preSum)):
            if i > 0:
                preSum[i] += preSum[i-1]
            if preSum[i] - curMin > maxSum:
                maxSum = preSum[i] - curMin
            preMS[i] = maxSum
            if preSum[i] < curMin:
                curMin = preSum[i]
           # print curMin
        del preMS[0]
        #print preMS
        
        surSum = nums[:] + [0]
        
        curMin = sys.maxint
        maxSum = nums[-1]
        for i in range(len(surSum)-1, -1, -1):
            if i != len(surSum) - 1:
                surSum[i] += surSum[i+1]
            if surSum[i] - curMin > maxSum:
                maxSum = surSum[i]- curMin
            postMS[i] = maxSum
            if surSum[i] < curMin:
                curMin = surSum[i]
        del postMS[-1]
        #print postMS
        
        result = - sys.maxint
        for i in range(len(preSum) -2):
            if preMS[i] + postMS[i + 1] > result:
                result = preMS[i] + postMS[i + 1]
        #if preMS[-1] > result:
        #    result = preMS[-1]
        return result
        
        