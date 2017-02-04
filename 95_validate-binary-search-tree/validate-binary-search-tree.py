# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/validate-binary-search-tree
@Language: Python
@Datetime: 16-11-08 08:04
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
#traverse
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """  
    result = True
    prev = -sys.maxint
    def isValidBST(self, root):
        # write your code here
        if not self.result or (root is None):
           return self.result
        self.isValidBST(root.left)
        if root.val > self.prev:
            self.prev = root.val
        else:
            self.result = False
            return False
        self.isValidBST(root.right)
        return self.result
            