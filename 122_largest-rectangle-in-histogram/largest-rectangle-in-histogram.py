# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/largest-rectangle-in-histogram
@Language: Python
@Datetime: 16-11-19 18:29
'''

class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        if len(height) == 0:
            return 0
        stack = []
        leftMin = [0 for _ in range(len(height))]
        # find the left first min for each 
        for i in range(len(height)):
            # stack[] [0] for height,[1] for index
            while len(stack) != 0 and stack[-1][0] >= height[i]:
                stack.pop()
            if len(stack) == 0:
                leftMin[i] = -1
            else:
                leftMin[i] = stack[-1][1]
            stack.append([height[i], i])   
        # find the right first min for each
        stack = []
        rightMin = [0 for _ in range(len(height))]
        for i in range(len(height)-1, -1, -1):
            # stack[] [0] for height,[1] for index
            while len(stack) != 0 and stack[-1][0] >= height[i]:
                stack.pop()
            if len(stack) == 0:
                rightMin[i] = len(height)
            else:
                rightMin[i] = stack[-1][1]
            stack.append([height[i], i])
        result = 0
        for i in range(len(height)):
            area = (rightMin[i] - leftMin[i] - 1) * height[i]
            if area > result:
                result = area
        return result
        
        
        