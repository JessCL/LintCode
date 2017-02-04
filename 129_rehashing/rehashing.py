# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/rehashing
@Language: Python
@Datetime: 16-11-23 04:56
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
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        capOld = len(hashTable)
        capNew = capOld * 2
        resultTable = [None] * capNew
        for i in range(capOld):
            node = hashTable[i]
            while node is not None:
                newHashCode = node.val % capNew
                if resultTable[newHashCode] is None:
                    resultTable[newHashCode] = ListNode(node.val)
                else:
                    node1 = resultTable[newHashCode]
                    while node1.next is not None:
                        node1 = node1.next
                    node1.next = ListNode(node.val)
                node = node.next
        return resultTable
                
                    
            
