# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/sqrtx
@Language: Python
@Datetime: 16-11-09 07:07
'''

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x == 1:
            return 1
        start = 0
        end = x / 2
        while start + 1 < end:
            mid = start + (end - start) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid
        if end * end <= x:
            return end
        if start * start <= x:
            return start
        return -1