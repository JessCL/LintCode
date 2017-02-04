# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/kth-smallest-number-in-sorted-matrix
@Language: Python
@Datetime: 16-12-20 05:13
'''

from heapq import *
class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        row = len(matrix)
        col = len(matrix[0])
        heap = []
        for i in range(row):
            heappush(heap, (matrix[i][0], i, 0))
        for _ in range(k-1):
            val, i, j = heappop(heap)
            j += 1
            if j < col:
                heappush(heap, (matrix[i][j], i, j))
        return heap[0][0]