# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/kth-largest-element
@Language: Python
@Datetime: 16-12-17 23:29
'''

class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if len(A) == 0:
            return -1
        return self.quickSelect(A, 0, len(A) - 1, k)
    def quickSelect(self, A, start, end, k):
        if start == end:
            return A[start]
        pivot = A[(start + end) / 2]
        i = start
        j = end
        while i <= j:
            while i <= j and A[i] > pivot:
                i += 1
            while i <= j and A[j] < pivot:
                j -= 1
            if  i <= j:
                swap = A[i]
                A[i] = A[j]
                A[j] = swap
                i += 1
                j -= 1
        if start + k - 1 <= j:
            return self.quickSelect(A, start, j, k)
        elif start + k - 1 >= i:
            return self.quickSelect(A, i, end , k - (i - start))
        else:
            return A[j + 1]
            
            
        