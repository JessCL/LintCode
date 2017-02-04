# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/triangle
@Language: Python
@Datetime: 16-12-09 22:57
'''

class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        for i in range(1, len(triangle)):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        
        minimum = sys.maxint
        for i in range(len(triangle)):
            if triangle[-1][i] < minimum:
                minimum = triangle[-1][i]
            
        return minimum