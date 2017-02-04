# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/add-two-numbers
@Language: Python
@Datetime: 16-12-16 23:40
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        dummy = ListNode(0)
        prev = dummy
        carry = 0
        while l1 is not None and l2 is not None:
            prev.next = ListNode((l1.val + l2.val + carry) % 10) 
            carry = (l1.val + l2.val + carry) / 10
            prev = prev.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            prev.next = ListNode((l1.val + carry) % 10) 
            carry = (l1.val + carry) / 10
            prev = prev.next
            l1 = l1.next
        while l2 is not None:
            prev.next = ListNode((l2.val + carry) % 10) 
            carry = (l2.val + carry) / 10
            prev = prev.next
            l2 = l2.next
        if carry > 0:
            prev.next = ListNode(carry) 
            prev = prev.next
            
        prev.next = None
        return dummy.next