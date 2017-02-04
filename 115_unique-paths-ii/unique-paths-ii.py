# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/unique-paths-ii
@Language: Python
@Datetime: 16-12-09 23:22
'''

class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        rowLen = len(obstacleGrid)
        colLen = len(obstacleGrid[0])
        dp = [[0 for _ in range(colLen)] for _ in range(rowLen)]
        
        for i in range(rowLen):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                break
            
        for j in range(colLen):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = 1
            else:
                break
         
        for i in range(1, rowLen):
            for j in range(1, colLen):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        
        return dp[-1][-1]