# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/minimum-depth-of-binary-tree
@Language: Python
@Datetime: 16-11-08 06:17
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
    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0
        return self.getMin(root)
        
    def getMin(self, root):
        if root is None:
            return sys.maxint
        if root.right is None and root.left is None:
            return 1
        return min(self.getMin(root.right), self.getMin(root.left)) + 1