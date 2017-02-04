# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/best-time-to-buy-and-sell-stock
@Language: Python
@Datetime: 16-12-20 22:45
'''

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        min = prices[0]
        result = 0
        for i in range(1,len(prices)):
            if prices[i] - min > result:
                result = prices[i] - min
            if prices[i] < min:
                min = prices[i]
        return result
        