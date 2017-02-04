# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/remove-duplicates-from-unsorted-list
@Language: Python
@Datetime: 16-11-15 06:27
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def removeDuplicates(self, head):
        s = set()
        curt = head
        dummy = ListNode(0, head)
        prev = dummy
        while curt is not None:
            if curt.val not in s:
                s.add(curt.val)
                curt = curt.next
                prev = prev.next
            else:
                curt = curt.next
                prev.next = curt
        return head  