# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/remove-duplicates-from-sorted-list-ii
@Language: Python
@Datetime: 16-11-15 00:40
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
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        start = head
        prev = dummy
        while start is not None:
            end = start.next
            if end is not None and start.val == end.val:
                end = end.next
                while end is not None and start.val == end.val:
                    end = end.next
                prev.next = end
                start = end
            else:
                prev = prev.next
                start = start.next
                
        return dummy.next
            
                
                