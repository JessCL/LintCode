# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/min-stack
@Language: Python
@Datetime: 16-11-19 17:54
'''

class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.minstack = []
        
    def push(self, number):
        # write yout code here
        self.stack.append(number)
        if  len(self.minstack) ==0 or number < self.minstack[-1]:
            self.minstack.append(number)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self):
        # pop and return the top item in stack
        result = self.stack[-1]
        del self.stack[-1]
        del self.minstack[-1]
        return result

    def min(self):
        # return the minimum number in stack
        return self.minstack[-1]