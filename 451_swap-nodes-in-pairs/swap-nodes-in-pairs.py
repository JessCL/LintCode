# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/swap-nodes-in-pairs
@Language: Python
@Datetime: 16-12-16 23:26
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        # ...prev->left->right->...
        if head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        left = head
        right = head.next
        
        while True:
            left.next = right.next
            right.next = left
            prev.next = right
            left = prev.next
            right = left.next
            
            if right.next is not None and right.next.next is not None:
                right = right.next.next
                left = left.next.next
                prev = prev.next.next
            else:
                break
        return dummy.next
        
        
        
        