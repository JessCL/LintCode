# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/intersection-of-two-arrays
@Language: Python
@Datetime: 16-11-18 17:47
'''

class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        s = set(nums1)
        resultSet = set()
        for i in nums2:
            if i in s:
                resultSet.add(i)
        return list(resultSet)
        