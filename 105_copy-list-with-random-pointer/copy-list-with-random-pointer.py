# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/copy-list-with-random-pointer
@Language: Python
@Datetime: 16-11-15 06:11
'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        hashmap = {}
        curt = head
        copyCurt = RandomListNode(curt.label)
        copyHead = copyCurt
        hashmap[curt] = copyCurt
        while curt.next is not None:
            copyCurt.next = RandomListNode(curt.next.label)
            curt = curt.next
            copyCurt = copyCurt.next
            hashmap[curt] = copyCurt

        copyCurt.next = None
        curt = head
        copyCurt = copyHead
        while curt is not None:
            if curt.random is not None:
                copyCurt.random = hashmap[curt.random]
            else:
                copyCurt.random = None
            curt = curt.next
            copyCurt = copyCurt.next
        return copyHead
        