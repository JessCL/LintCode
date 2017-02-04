# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/palindrome-partitioning-ii
@Language: Python
@Datetime: 16-12-14 20:09
'''

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        n = len(s)
        if (n == 0):
            return -1
        isP = [[False for _ in range(n)] for _ in range(n)]
        # isP[i,j] represent wether s[i:j+1] is Palindrome
        for i in range(n):
            isP[i][i] = True
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if j == i+1:
                    isP[i][j] = (s[i] == s[j])
                else:
                    isP[i][j] = (isP[i+1][j-1] and (s[i] == s[j]))
        #print isP           
        dp = [0]*n
        for i in range(n):
            if isP[0][i]:
                dp[i] = 0
            else:
                dp[i] = i
        #dp[i] reprent the mincut for s[0:i+1]
        for i in range(1, n):
            for j in range(i, 0, -1):
                if isP[j][i]:
                    dp[i] = min(dp[i], dp[j-1] + 1)  
        #print dp
        return dp[-1]
        
        