# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iii
@Language: Python
@Datetime: 16-12-20 23:33
'''

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        # write your code here
        preMP = [0] * len(prices)  # åæ¬ç¬¬iå¤©
        postMP = [0] * len(prices) # åæ¬ç¬¬iå¤© 
        curMin = prices[0]
        maxPro = 0
        for i in range(len(prices)):
            if prices[i] < curMin:
                curMin = prices[i]
            if prices[i] - curMin > maxPro:
                maxPro = prices[i] - curMin
            preMP[i] = maxPro
        #print preMP
        curMax = prices[-1]
        maxPro = 0
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > curMax:
                curMax = prices[i]
            if  curMax - prices[i] > maxPro:
                maxPro = curMax - prices[i]
            postMP[i] = maxPro
        #print postMP
        result = 0
        for i in range(len(prices) -1):
            if preMP[i] + postMP[i + 1] > result:
                result = preMP[i] + postMP[i + 1]
        if preMP[-1] > result:
            result = preMP[-1]
        return result