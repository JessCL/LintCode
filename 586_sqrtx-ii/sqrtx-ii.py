# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/sqrtx-ii
@Language: Python
@Datetime: 16-11-22 20:37
'''

class Solution:
    # @param {double} x a double
    # @return {double} the square root of x
    def sqrt(self, x):
        if x == 0:
            return 0
        
        start = 0.0
        if x < 1:
            end = 1
        else:
            end = x
        while (end - start) > 0.00000000001:
            mid = (end + start) / 2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                end = mid
            else:
                start = mid
        return end
    
            