# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/binary-tree-inorder-traversal
@Language: Python
@Datetime: 16-11-07 19:52
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
    @return: Inorder in ArrayList which contains node values.
    """
    class popNode:
        def __init__(self, node):
            self.val = node.val
            self.left = node.left
            self.right = node.right
            self.popTimes = 0
            
    def inorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        popRoot = self.popNode(root)
        stack = []
        result = []
        stack.append(popRoot)
        while len(stack) != 0:
            popRoot = stack[-1]
            del stack[-1]
            if popRoot.popTimes == 0:
                popRoot.popTimes += 1
                if popRoot.right is not None:
                    stack.append(self.popNode(popRoot.right))
                stack.append(popRoot)
                if popRoot.left is not None:
                    stack.append(self.popNode(popRoot.left))
            else:
                result.append(popRoot.val)
        return result
        