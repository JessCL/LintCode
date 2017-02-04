# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/wood-cut
@Language: Python
@Datetime: 16-11-09 05:36
'''

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if len(L) == 0 or k == 0:
            return 0
            
        end = sum(L) / k
        start = 1
        if end == 0:
            return 0
        while start + 1 < end:
            mid = start + (end - start) / 2
            kk = 0
            for i in L:
                kk += i / mid 
            if kk >= k:
                start = mid
            else:
                end = mid

        kk = 0        
        for i in L:
            kk += i / end
        if kk >= k:
            return end
        kk = 0        
        for i in L:
            kk += i / start
        if kk >= k:
            return start
        return 0
        