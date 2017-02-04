# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/subarray-sum-closest
@Language: Python
@Datetime: 16-11-18 22:31
'''

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        if len(nums) <=1:
            return [0,0]
        prefixSum = []
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            prefixSum.append([tmp,i])
        prefixSum.sort()
        minDiff = sys.maxint
        minDiffIndex = -1
        for i in range(len(prefixSum)-1):
            if abs(prefixSum[i][0]-prefixSum[i+1][0]) < minDiff:
                minDiff = abs(prefixSum[i][0]-prefixSum[i+1][0])
                minDiffIndex = i
        return [min(prefixSum[minDiffIndex][1],prefixSum[minDiffIndex+1][1])+1,max(prefixSum[minDiffIndex][1],prefixSum[minDiffIndex+1][1])]
                