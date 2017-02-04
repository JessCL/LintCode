# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/reverse-linked-list-ii
@Language: Python
@Datetime: 16-11-15 01:14
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
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0, head)
        prev = dummy
        for i in range(m-1):
            prev = prev.next
        curt = prev.next
        prev.next = self.reverse(curt, n - m + 1)
        return dummy.next
        
    def reverse(self, head, k):
        if k == 1:
            return head
        prev = head
        curt = head.next
        post = curt.next
        for i in range(k-1):
            curt.next = prev
            prev = curt
            curt = post
            if post is not None:
                post = post.next
        head.next = curt
        return prev