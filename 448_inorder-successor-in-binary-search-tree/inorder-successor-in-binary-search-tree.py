# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/inorder-successor-in-binary-search-tree
@Language: Python
@Datetime: 16-11-10 19:23
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        result = None
        while root is not None:
            if root.val > p.val:
                result = root
                root = root.left
            else:
                root = root.right
                
        return result
                
        