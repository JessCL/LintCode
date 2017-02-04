# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/unique-paths
@Language: Python
@Datetime: 16-12-09 23:15
'''

class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+ dp[i][j-1] 
        return dp[-1][-1]