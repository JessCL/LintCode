# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/lowest-common-ancestor-ii
@Language: Python
@Datetime: 16-11-23 23:58
'''

"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""
class Solution:
    """
    @param root: The root of the tree
    @param A and B: Two node in the tree
    @return: The lowest common ancestor of A and B
    """ 
    def lowestCommonAncestorII(self, root, A, B):
        pathA = []
        self.findPath(pathA, A, root)
        pathB = []
        self.findPath(pathB, B, root)
        indexA = len(pathA) - 1
        indexB = len(pathB) - 1 
        while indexA >= 0 and indexB >= 0 and pathA[indexA] == pathB[indexB]:
            indexA -= 1
            indexB -= 1
        return pathA[indexA + 1]
        
    def findPath(self, path, node, root):
        while node != root:
            path.append(node)
            node = node.parent
        path.append(node)
        
