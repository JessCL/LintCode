# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/ugly-number-ii
@Language: Python
@Datetime: 16-12-17 07:22
'''

from heapq import *
class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        pQueue = []
        heappush(pQueue,1)
        s = set()
        s.add(1)
        count = 0 
        for i in range(n):
            current = heappop(pQueue)
            if (current * 2) not in s:
                s.add(current * 2)
                heappush(pQueue, current * 2)
            if (current * 3) not in s:
                s.add(current * 3)
                heappush(pQueue, current * 3)
            if (current * 5) not in s:
                s.add(current * 5)
                heappush(pQueue, current * 5)
        return current

            
