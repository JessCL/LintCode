# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/divide-two-integers
@Language: Python
@Datetime: 17-01-06 05:54
'''

class Solution:
    # @param {int} dividend the dividend
    # @param {int} divisor the divisor
    # @return {int} the result
    def divide(self, dividend, divisor):
        if divisor == 0:
            return 2147483647
        
        if (dividend < 0) ^ (divisor < 0):
            sign = -1
        else:
            sign = 1
           
        dividend =  abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        while divisor <= dividend:
            cnt = 0
            while (divisor << cnt) <= dividend:
                cnt += 1
            cnt -= 1
            result += 2**cnt
            dividend = dividend - divisor * (2**cnt)
            
        else:
            if sign*result > 2147483647 or sign*result < -2147483648:
                return 2147483647
            return sign*result
        