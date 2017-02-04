# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/longest-substring-without-repeating-characters
@Language: Python
@Datetime: 17-01-06 06:56
'''

class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        # write your code here
        hash = {}
        start = 0
        result = 0
        for end in range(len(s)):
            if hash.has_key(s[end]):
                while s[start] != s[end]:
                    del hash[s[start]]
                    start += 1
                start += 1
                hash[s[end]] = end
                
            else:
                hash[s[end]] = end
                if end - start + 1 > result:
                    result = end - start + 1
            #print start, end      
                
        return result