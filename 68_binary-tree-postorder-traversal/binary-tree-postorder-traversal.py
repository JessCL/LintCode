# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/binary-tree-postorder-traversal
@Language: Python
@Datetime: 16-11-07 20:05
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# non-recursion, using list to contain node and popTimes
class Solution:
    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        result = []
        stack = []
        stack.append([root, 0])
        while len(stack) != 0:
            rootList = stack[-1]
            if rootList[1] == 0:
                rootList[1] += 1
                if rootList[0].right is not None:
                    stack.append([rootList[0].right, 0])
                if rootList[0].left is not None:
                    stack.append([rootList[0].left, 0])    
            else:
                result.append(rootList[0].val)
                del stack[-1]
        return result
                