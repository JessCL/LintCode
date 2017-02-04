# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/merge-k-sorted-arrays
@Language: Python
@Datetime: 16-12-17 23:48
'''

from heapq import *
class Solution:
    # @param {int[][]} arrays k sorted integer arrays
    # @return {int[]} a sorted array
    def mergekSortedArrays(self, arrays):
        heap = []
        result = []
        for index, array in enumerate(arrays):
            if len(array):
                heappush(heap, (array[0], index, 0))
        while len(heap):
            val, i, j = heappop(heap)
            result.append(val)
            j += 1
            if j < len(arrays[i]):
                heappush(heap, (arrays[i][j], i, j))
        return result
                
        
            