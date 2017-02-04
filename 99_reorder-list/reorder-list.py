# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/reorder-list
@Language: Python
@Datetime: 16-11-15 22:56
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
    @return: nothing
    """
    def reorderList(self, head):
        if head is None or head.next is None:
            return head
        mid = self.middleOfList(head)
        rightHead = self.reverse(mid.next)
        mid.next = None
        curt = ListNode(0)
        left = head
        right = rightHead
    
        while right is not None and left is not None:
            curt.next = left
            curt = curt.next
            left = left.next
            curt.next = right
            curt = curt.next
            right = right.next
    
        if left is not None:
            curt.next = left
            curt = curt.next
        if right is not None:
            curt.next = right
            curt = curt.next
        curt.next = None

    def middleOfList(self, head):
        if head is None or head.next is None:
            return head
        fast = head.next
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        if head.next is None:
            return head
        prev = head
        curt = head.next
        post = curt.next
        prev.next = None
        while post is not None:
            curt.next = prev
            prev = curt
            curt = post
            post = post.next
        curt.next = prev
        return curt

        