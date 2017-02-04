# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/single-number
@Language: Python
@Datetime: 16-12-24 19:33
'''

class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        if len(A) == 0:
            return 0
        result = A[0]
        for num in A[1:]:
            result ^= num
        return result
        
        '''
        if len(A) == 0:
            return 0
        s = set()
        for num in A:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return s.pop()
        '''
        