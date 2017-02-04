# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/binary-tree-level-order-traversal
@Language: Python
@Datetime: 16-11-26 20:04
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
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        queue = []
        if root is None:
            return queue
        queue.append(root)
        result = []
        while len(queue) > 0:
            result.append([])
            nextlevel = []
            for current in queue:
                if current.left is not None:
                    nextlevel.append(current.left)
                if current.right is not None:
                    nextlevel.append(current.right)
                result[-1].append(current.val)
            queue = nextlevel[:]
        return result
                
            