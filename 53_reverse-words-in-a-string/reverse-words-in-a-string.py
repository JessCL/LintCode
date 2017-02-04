# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/reverse-words-in-a-string
@Language: Python
@Datetime: 16-12-24 19:10
'''

class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        s = s.strip()
        i = 0
        s = list(s)
        while i < len(s):
            if s[i] == ' ':
                i += 1
                while s[i] == ' ':
                    del s[i]
            i += 1
        #print "".join(s)
        self.reverse(0, len(s) - 1, s)
        #print s
        start = 0
        i = 0 
        for i in range(len(s)):
            if s[i] == ' ':
                end = i - 1
                self.reverse(start, end, s)
                start = i + 1
        self.reverse(start, len(s) - 1, s)  
        return "".join(s)
   
    def reverse(self, start, end, s):     
        while start < end:
            swap = s[start]
            s[start] = s[end]
            s[end] = swap
            start += 1
            end -= 1
            