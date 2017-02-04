# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/binary-search-tree-iterator
@Language: Python
@Datetime: 16-11-09 06:34
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""
#non-recursion
class BSTIterator:
    #@param root: The root of binary tree.
    stack = []
    def __init__(self, root):
        if root is not None:
            self.stack.append([root, 0])
            
    #@return: True if there has next node, or false
    def hasNext(self):
        if len(self.stack) != 0:
            return True
        else:
            return False
            
    #@return: return next node
    def next(self):
        while len(self.stack) != 0:
            root = self.stack[-1]
            del self.stack[-1]
            if root[1] == 0:
                if root[0].right is not None:
                    self.stack.append([root[0].right, 0])
                self.stack.append([root[0], 1])
                if root[0].left is not None:
                    self.stack.append([root[0].left, 0])
            else:
               return root[0]
                
        else:
            return None