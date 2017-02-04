# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/search-for-a-range
@Language: Python
@Datetime: 16-11-10 07:00
'''

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if len(A) == 0:
            return [-1, -1]
        start = 0
        end = len(A) - 1
        first = -1
        # find the first position of target
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                if mid == 0 or A[mid - 1] != target:
                    first = mid
                    break
                else:
                    end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if first == -1:
            if A[start] == target:
                first = start
            elif A[end] == target:
                first = end
        if first == -1:
            return [-1, -1]
        start = first  
        end = len(A) - 1
        last = -1
        # find the last position of target
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                if mid == (len(A) - 1) or A[mid + 1] != target:
                    last = mid
                    break
                else:
                    start = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if last == -1:
            if A[end] == target:
                last = end
            elif A[start] == target:
                last = start
        
        return [first, last]
                
        