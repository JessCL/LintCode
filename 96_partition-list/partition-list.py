# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/partition-list
@Language: Python
@Datetime: 16-11-15 01:32
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
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        leftDummy = ListNode(0)
        leftCurt = leftDummy
        rightDummy = ListNode(0)
        rightCurt = rightDummy
        curt = head
        while curt is not None:
            if curt.val < x:
                #leftCurt.next = ListNode(curt.val)
                #leftCurt = leftCurt.next
                leftCurt.next = curt
                leftCurt = curt
            else:
                #rightCurt.next = ListNode(curt.val)
                #rightCurt = rightCurt.next
                rightCurt.next = curt
                rightCurt = curt
            curt = curt.next
        leftCurt.next = rightDummy.next
        rightCurt.next = None  #very important!!
        return leftDummy.next
            