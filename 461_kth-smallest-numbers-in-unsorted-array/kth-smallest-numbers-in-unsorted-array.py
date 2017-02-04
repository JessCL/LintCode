# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/kth-smallest-numbers-in-unsorted-array
@Language: Python
@Datetime: 16-11-22 21:07
'''

import heapq
class Solution:
    # @param {int} k an integer
    # @param {int[]} nums an integer array
    # return {int} kth smallest element
    def kthSmallest(self, k, nums):
        # Write your code here
        heapq.heapify(nums)
        topk = heapq.nsmallest(k, nums)
        topk.sort()
        return topk[k-1]