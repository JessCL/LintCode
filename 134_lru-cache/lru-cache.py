# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/lru-cache
@Language: Python
@Datetime: 16-12-31 19:14
'''

class LinkedNode():
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.next = None
        
class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity
        
    def push_back(self, node):
        self.tail.next = node
        self.hash[node.key] = self.tail
        self.tail = node
        
    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head
        
    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):
        node = prev.next
        #node.value = value
        if node != self.tail:
            node = prev.next
            prev.next = node.next
            self.hash[prev.next.key] = prev
            
            node.next = None
            self.push_back(node)

    # @return an integer
    def get(self, key):
        if self.hash.has_key(key):
            value = self.hash[key].next.value
            self.kick(self.hash[key])
            #self.printLink()
            return value
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.hash.has_key(key):
            self.kick(self.hash[key])
            self.hash[key].next.value = value
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.hash) > self.capacity:
                #print True
                self.pop_front()
        #self.printLink()
        
    def printLink(self):
        node = self.head.next
        while node is not None:
            print node.key, ",", node.value, "->",
            node = node.next
        print