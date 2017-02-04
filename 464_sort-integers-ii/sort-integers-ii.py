# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/sort-integers-ii
@Language: Python
@Datetime: 16-11-18 20:08
'''

class Solution():
    # @param {int[]} A an integer array
    # @return nothing
    # quickSort
    def sortIntegers2(self, A):
        if len(A) == 0:
            return 
        self.quickSort(A, 0, len(A) - 1)

    def quickSort(self, A, start, end):
        if start >= end:
            return
        # point 1: pivot, get the value not index
        left = start
        right = end
        pivot = A[(start + end) / 2]
        # point 2: left<=right not left < right
        while left <= right:
            # point 3: A[left] < pivot not <=
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                temp = A[left]
                A[left] = A[right]
                A[right] = temp
                left += 1
                right -= 1
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)
        