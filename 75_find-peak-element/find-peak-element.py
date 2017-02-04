# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/find-peak-element
@Language: Python
@Datetime: 16-11-09 06:08
'''

class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        end = len(A) - 1
        start = 0
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] > A[mid-1] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid] > A[mid-1]:
                start = mid
            else:
                end = mid
        '''        
        if A[start] > A[end]:
            return start
        else:
            return end
        '''
        return -1