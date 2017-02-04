# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/search-range-in-binary-search-tree
@Language: Python
@Datetime: 16-11-10 19:31
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
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        path = []
        self.inOrder(root, path, k1, k2)
        return path
        
    def inOrder(self, root, path, k1, k2):
        if root is None:
            return
        self.inOrder(root.left, path, k1, k2)
        if k1 <= root.val and root.val <= k2:
            path.append(root.val)
        self.inOrder(root.right, path, k1, k2)
        