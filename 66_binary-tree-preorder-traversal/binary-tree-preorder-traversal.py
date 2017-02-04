# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/binary-tree-preorder-traversal
@Language: Python
@Datetime: 16-11-07 17:57
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# non-recursion
class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        stack = []
        result = []
        if root is not None:
            stack.append(root)
        else:
            return result
        while len(stack) != 0:
            root = stack[-1]
            del stack[-1]                 #pop
            result.append(root.val)
            if root.right is not None:
                stack.append(root.right)  #push
            if root.left is not None:
                stack.append(root.left)   #push
        return result    
        