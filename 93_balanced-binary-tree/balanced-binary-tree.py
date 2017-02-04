# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/balanced-binary-tree
@Language: Python
@Datetime: 16-11-02 03:09
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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        result, height = self.Helper(root)
        return result
        
    def Helper(self, root):
        # return type:is A Balanced Tree, Height
        if root is None:
            return True, 0
            
        isBalanceLeft, heightLeft = self.Helper(root.left) 
        isBalanceRight, heightRight = self.Helper(root.right) 
    
        if isBalanceLeft and isBalanceRight and abs(heightLeft-heightRight) <= 1:
            return True, max(heightLeft, heightRight) + 1
        else:
            return False, -1