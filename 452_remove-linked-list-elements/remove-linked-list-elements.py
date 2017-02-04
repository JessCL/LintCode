# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/remove-linked-list-elements
@Language: Python
@Datetime: 16-12-16 20:50
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curt = head
        while curt is not None:
            if curt.val == val:
                curt = curt.next
                prev.next = curt
            else:
                prev = curt
                curt = curt.next
        return dummy.next
                
                