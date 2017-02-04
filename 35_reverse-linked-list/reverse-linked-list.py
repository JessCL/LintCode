# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/reverse-linked-list
@Language: Python
@Datetime: 16-11-15 00:51
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
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        prev = head
        curt = head.next
        head.next = None
        post = curt.next
        while post is not None:
            curt.next = prev
            prev = curt
            curt = post
            post = curt.next
        curt.next = prev
        return curt