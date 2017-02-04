# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/top-k-largest-numbers-ii
@Language: Python
@Datetime: 16-12-17 22:33
'''

from heapq import *
class Solution:

    # @param {int} k an integer
    def __init__(self, k):
        # initialize your data structure here.
        self.k = k
        self.sizeOfheap = 0
        self.heap = []
        
        
    # @param {int} num an integer
    def add(self, num):
        # Write your code here
        if self.sizeOfheap == self.k:
            if num > self.heap[0]:
                heapreplace(self.heap, num)
        else:
            heappush(self.heap, num)
            self.sizeOfheap += 1

    # @return {int[]} the top k largest numbers
    def topk(self):
        # Write your code here
        return sorted(self.heap, reverse = True)

