# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/maximal-rectangle
@Language: Python
@Datetime: 16-11-19 19:54
'''

class Solution:
    # @param {boolean[][]} matrix, a list of lists of boolean
    # @return {int} an integer
    class stackType:
        def __init__(self, val, index):
            self.val = val
            self.index = index
        
    def maximalRectangle(self, matrix):
        
        rowL = len(matrix)
        if rowL == 0:
            return 0
        colL = len(matrix[0])
        result = 0
        # find accumulate maxtrix
        for col in range(colL):
            for row in range(rowL):
                if row > 0 and matrix[row][col] ==1:
                    matrix[row][col] = matrix[row-1][col] + 1

        for row in range (rowL):
            stack = []
            leftMin = [-1 for _ in range(colL)]
            rightMin = [-1 for _ in range(colL)]
            # find left first min (index)
            for i in range(colL):
                while len(stack) != 0 and stack[-1].val >= matrix[row][i]:
                    stack.pop()
                if len(stack) == 0:
                    leftMin[i] = -1
                else:
                    leftMin[i] = stack[-1].index
                stack.append(self.stackType(matrix[row][i], i))
            
            stack = []
            # find right first min (index)
            for i in range(colL-1, -1, -1):
                while len(stack) != 0 and stack[-1].val >= matrix[row][i]:
                    stack.pop()
                if len(stack) == 0:
                    rightMin[i] = colL
                else:
                    rightMin[i] = stack[-1].index
                stack.append(self.stackType(matrix[row][i], i))
                
            for i in range(colL):
                area = (rightMin[i] - leftMin[i] - 1) * matrix[row][i]
                if area > result:
                    result = area
        return result
                    