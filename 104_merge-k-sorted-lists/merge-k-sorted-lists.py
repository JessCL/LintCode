# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/merge-k-sorted-lists
@Language: Python
@Datetime: 16-12-17 23:57
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
from heapq import *
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        numL = len(lists)
        dummy = ListNode(0)
        prev = dummy
        heap = []
        
        for index, head in enumerate(lists):
            if head is not None:
                heappush(heap, (head.val, head.next))

        while len(heap):
            val, head = heappop(heap)
            prev.next = ListNode(val)
            prev = prev.next
            if head is not None:
                heappush(heap, (head.val, head.next))
                
        return dummy.next
        
            
            
        
        

