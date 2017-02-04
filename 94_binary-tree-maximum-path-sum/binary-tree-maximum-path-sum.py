# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/binary-tree-maximum-path-sum
@Language: Python
@Datetime: 16-11-10 17:58
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        if root is None:
            return 0
        rootMax, rootSingle = self.Helper(root)
        return rootMax
        
    def Helper(self, root):
        if root is None:
            return -sys.maxint, -sys.maxint
        leftMax, leftSingle = self.Helper(root.left)
        rightMax, rightSingle = self.Helper(root.right)
        rootSingle = max(leftSingle, rightSingle, 0) + root.val
        rootMax = max(leftMax, rightMax, rootSingle, leftSingle + rightSingle + root.val)
        return rootMax, rootSingle
        
        