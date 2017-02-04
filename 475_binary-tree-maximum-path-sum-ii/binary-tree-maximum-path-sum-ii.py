# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/binary-tree-maximum-path-sum-ii
@Language: Python
@Datetime: 16-11-08 06:46
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root the root of binary tree.
    @return an integer
    """
    def maxPathSum2(self, root):
        # Write your code here
        if root is None:
            return 0
        return max(self.maxPathSum2(root.left), self.maxPathSum2(root.right), 0) + root.val