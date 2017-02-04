# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/minimum-path-sum
@Language: Python
@Datetime: 16-12-09 23:09
'''

class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        rowLen = len(grid)
        colLen = len(grid[0])
        for i in range(1, rowLen):
            grid[i][0] += grid[i-1][0]
        for j in range(1, colLen):
            grid[0][j] += grid[0][j-1]
            
        for i in range(1, rowLen):
            for j in range(1,colLen):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        
        return grid[rowLen-1][colLen-1]
            