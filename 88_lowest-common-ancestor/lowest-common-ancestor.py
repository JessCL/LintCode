# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/lowest-common-ancestor
@Language: Python
@Datetime: 16-11-24 00:29
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        if A == root or B == root:
            return root
        leftA = self.find(root.left, A)
        leftB = self.find(root.left, B)
        if leftA and leftB:
            return self.lowestCommonAncestor(root.left, A, B)
        elif not leftA and not leftB:
            return self.lowestCommonAncestor(root.right, A, B)
        else:
            return root

    def find(self, root, target):
        if root is None:
            return False
        if root == target:
            return True
        return self.find(root.left, target) or self.find(root.right, target)