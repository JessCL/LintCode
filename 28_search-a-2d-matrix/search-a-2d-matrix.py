# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/search-a-2d-matrix
@Language: Python
@Datetime: 16-10-29 05:08
'''

class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        rowNum = len(matrix)
        colNum = len(matrix[0])

        start = 0
        end = colNum * rowNum - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            row = mid / colNum
            col = mid % colNum
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                start = mid
            else:
                end = mid

        if matrix[start / colNum][start % colNum] == target:
            return True
        if matrix[end / colNum][end % colNum] == target:
            return True
        return False
