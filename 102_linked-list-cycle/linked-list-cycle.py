# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/linked-list-cycle
@Language: Python
@Datetime: 16-11-15 03:21
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
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        dummy = ListNode(0, head)
        fast = head
        slow = head
        while fast is not None and slow is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            slow = slow.next
            if fast is not None and fast == slow:
                return True
        return False
