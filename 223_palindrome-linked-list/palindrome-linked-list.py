# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/palindrome-linked-list
@Language: Python
@Datetime: 16-12-17 05:32
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        slow = head
        fast = head.next
        stack = []
        stack.append(slow.val)
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)
            
        if fast is None: #odd size
            del stack[-1]
        #else: #even size
        slow = slow.next
        while slow is not None :
            if slow.val != stack[-1]:
                return False
            del stack[-1]
            slow = slow.next

        return True
            