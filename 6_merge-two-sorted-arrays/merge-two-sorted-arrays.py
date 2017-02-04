# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/merge-two-sorted-arrays
@Language: Python
@Datetime: 16-11-13 06:19
'''

class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        indexA = 0
        indexB = 0
        lenA = len(A)
        lenB = len(B)
        result = []
        while indexA < lenA and indexB < lenB:
            if A[indexA] < B[indexB]:
                result.append(A[indexA])
                indexA += 1
            elif A[indexA] > B[indexB]:
                result.append(B[indexB])
                indexB += 1
            else:
                result.append(A[indexA])
                result.append(B[indexB])
                indexA += 1
                indexB += 1
        while indexA < lenA:
            result.append(A[indexA])
            indexA += 1
        while indexB < lenB:
            result.append(B[indexB])
            indexB += 1
        return result
            