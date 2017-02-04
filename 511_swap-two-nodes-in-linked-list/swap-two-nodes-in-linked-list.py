# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/swap-two-nodes-in-linked-list
@Language: Python
@Datetime: 16-12-17 00:22
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head, a ListNode
    # @oaram {int} v1 an integer
    # @param {int} v2 an integer
    # @return {ListNode} a new head of singly-linked list
    def swapNodes(self, head, v1, v2):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        prev1 = None
        prev2 = None
        while prev.next is not None:
            if prev.next.val == v1:
                prev1 = prev
                prev = prev.next
                while prev.next is not None:
                    if prev.next.val == v2:
                        prev2 = prev
                        break
                    else:
                        prev = prev.next
                break
                
            elif prev.next.val == v2:
                prev1 = prev
                prev = prev.next
                while prev.next is not None:
                    if prev.next.val == v1:
                        prev2 = prev
                        break
                    else:
                        prev = prev.next
                break
            else:
                prev = prev.next
        if prev1 is not None and prev2 is not None:
            if prev1.next == prev2:
                node1 = prev1.next
                node2 = prev2.next
                post2 = node2.next
                prev1.next = node2
                node2.next = node1
                node1.next = post2
            else:
                # ...prev1->node1->post1->...->prev2->node2->post2->...
                node1 = prev1.next
                node2 = prev2.next
                post1 = node1.next
                post2 = node2.next
                prev1.next = node2
                node2.next = post1
                prev2.next = node1
                node1.next = post2
        return dummy.next
            
            
