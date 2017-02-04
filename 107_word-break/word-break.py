# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/word-break
@Language: Python
@Datetime: 16-12-10 00:34
'''

class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        n = len(s)
        L = 0
        for i in dict:
            L = max(L, len(i))
        # dp[i] can the first i characters be perfectly break
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i-1, max(i-L-1, -1), -1):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
                    break
        return dp[-1]
