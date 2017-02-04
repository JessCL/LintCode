# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/merge-two-sorted-lists
@Language: Python
@Datetime: 16-12-16 21:47
'''

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    #without extra space
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        lastNode = dummy
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                lastNode.next = l1
                l1 = l1.next
            else:
                lastNode.next = l2
                l2 = l2.next
            lastNode = lastNode.next
        
        if l1 is not None:
            lastNode.next = l1
        else:
            lastNode.next = l2
        return dummy.next