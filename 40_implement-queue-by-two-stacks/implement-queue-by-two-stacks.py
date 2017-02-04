# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/implement-queue-by-two-stacks
@Language: Python
@Datetime: 17-01-02 00:25
'''

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def ST1FlipToST2(self):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        
    def push(self, element):
        self.stack1.append(element)
        
    def top(self):
        # return the top element
        if len(self.stack2) == 0:
            self.ST1FlipToST2()
        return self.stack2[-1]  
        
    def pop(self):
        # pop and return the top element
        if len(self.stack2) == 0:
            self.ST1FlipToST2()
        return self.stack2.pop()
