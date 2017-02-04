# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/max-tree
@Language: Python
@Datetime: 16-11-19 19:02
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class stackType:
    def __init__(self, val, index):
        self.val = val
        self.index = index
class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        nodeList = [TreeNode(i) for i in A]
        leftFirstLarger = [-1 for _ in A]
        rightFirstLarger = [-1 for _ in A]
        stack = []
        # find the leftFirstLargerIndex for each
        for i in range(len(A)):
            while len(stack) != 0 and stack[-1].val < A[i]:
                stack.pop()
            if len(stack) == 0:
                leftFirstLarger[i] = -1
            else:
                leftFirstLarger[i] = stack[-1].index
            stack.append(stackType(A[i], i))
        #find the rightFirstLargerIndex for each
        stack = []
        for i in range(len(A)-1, -1, -1):
            while len(stack) != 0 and stack[-1].val < A[i]:
                stack.pop()
            if len(stack) == 0:
                rightFirstLarger[i] = -1
            else:
                rightFirstLarger[i] = stack[-1].index
            stack.append(stackType(A[i], i))
        for i in range(len(A)):
            if leftFirstLarger[i] == -1 and rightFirstLarger[i] == -1:
                root = nodeList[i]
            elif leftFirstLarger[i] != -1 and  rightFirstLarger[i] == -1: 
                nodeList[leftFirstLarger[i]].right = nodeList[i]
            elif leftFirstLarger[i] == -1 and  rightFirstLarger[i] != -1:
                nodeList[rightFirstLarger[i]].left = nodeList[i]
            else:# if leftFirstLarger[i] != -1 and  rightFirstLarger[i] != -1:
                if A[rightFirstLarger[i]] < A[leftFirstLarger[i]]:
                    nodeList[rightFirstLarger[i]].left = nodeList[i]
                else:
                    nodeList[leftFirstLarger[i]].right = nodeList[i]
        return root
            
                
            
        
        