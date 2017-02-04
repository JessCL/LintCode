# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/insert-node-in-a-binary-search-tree
@Language: Python
@Datetime: 16-11-10 19:44
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
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        originRoot = root
        
        if root is None:
            root = node
            return root
            
        while True:
            if node.val > root.val:
                if root.right is None:
                    root.right = node
                    break
                else:
                    root = root.right
            else:
                if root.left is None:
                    root.left = node
                    break
                else:
                    root = root.left
                    
        return originRoot
                
        