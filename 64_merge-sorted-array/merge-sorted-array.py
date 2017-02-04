# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/merge-sorted-array
@Language: Python
@Datetime: 16-12-20 19:59
'''

class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        while m >= 1 and n >= 1 :
            if A[m-1] > B[n-1]:
                A[m + n -1] = A[m-1]
                m = m - 1
            else:
                A[m + n -1] = B[n-1]
                n = n - 1 
        while n >= 1:
            A[n - 1] = B[n - 1]
            n = n - 1
            
        
        
        
        