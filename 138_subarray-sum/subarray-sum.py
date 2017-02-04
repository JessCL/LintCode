# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/subarray-sum
@Language: Python
@Datetime: 16-11-18 22:09
'''

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        hashTable = {0: [-1]}
        prefixSum = 0
        result = []
        for i in range(len(nums)):
            prefixSum += nums[i]
            if hashTable.has_key(prefixSum):
                for j in hashTable[prefixSum]:
                    result.append([j+1, i])
                hashTable[prefixSum] += [i]
            else:
                hashTable[prefixSum] = [i]
        return result[0]
            