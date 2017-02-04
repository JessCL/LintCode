# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/linked-list-cycle-ii
@Language: Python
@Datetime: 16-11-15 03:30
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
    @return: The node where the cycle begins. 
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        fast = head
        slow = head
        pointer = head
        while fast is not None and fast.next is not None and slow is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is not None:
                if fast == slow:
                    while slow !=pointer:
                        slow = slow.next
                        pointer = pointer.next
                    return pointer
            else:
                return None
        else:
            return None