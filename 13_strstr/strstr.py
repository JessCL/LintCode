# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/strstr
@Language: Python
@Datetime: 16-10-22 19:50
'''

class Solution:
    def strStr(self, source, target):
        if source == None:
            return -1
        if target == None:
            return -1
        if len(target) == 0:
            return 0
        if len(source) ==0:
            return -1

        i = j = 0
        while i + j < len(source):
            while i + j < len(source) and j < len(target) and source[i + j] == target[j]:
                j += 1
            if j == len(target):
                return i
            j = 0
            i += 1
        return -1