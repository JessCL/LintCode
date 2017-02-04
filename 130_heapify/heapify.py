# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/heapify
@Language: Python
@Datetime: 16-11-23 23:36
'''

class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapSwiftUp(self, heap, target):
        # siftup
        while (target - 1) / 2 >= 0 and heap[target] < heap[(target -1) / 2]:
            swap =  heap[target]
            heap[target] = heap[(target -1) / 2]
            heap[(target -1) / 2] = swap
            target = (target -1) / 2
        
    def heapify(self, A):
        for i in range(len(A)):
            self.heapSwiftUp(A, i)


        
            