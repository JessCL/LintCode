# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/convert-sorted-list-to-balanced-bst
@Language: Python
@Datetime: 16-12-16 20:41
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        return self.helper(head, None)
        #print self.findMid(head, None).val
        
    def helper(self, start, end):
        if start == end:
            return None
            
        mid = self.findMid(start, end)
        #print mid.val
        current = TreeNode(mid.val)
        current.left = self.helper(start, mid)
        current.right = self.helper(mid.next, end)
        return current
        
    
    def findMid(self, start, end):
        if start == end or start.next == end:
            return start
        fast = start.next
        slow = start
        while fast != end and fast.next != end:
            fast = fast.next.next
            slow = slow.next
        return slow