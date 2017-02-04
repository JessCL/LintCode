# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/sort-letters-by-case
@Language: Python
@Datetime: 16-12-21 22:09
'''

class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        start = 0
        end = len(chars) - 1
        while start <= end:
            while start <= end and chars[start].islower():
                start += 1
            while start <= end and chars[end].isupper():
                end -= 1
            #print start, end
            if start <= end:
                swap = chars[end]
                chars[end] = chars[start]
                chars[start] = swap
                start += 1
                end -= 1
        #print chars
        return chars
    
