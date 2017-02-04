# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/palindrome-partitioning
@Language: Python
@Datetime: 16-12-22 19:50
'''

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        #print self.isPalindrome(s)
    
        results = []
        self.Helper(results, [], s, 0)
        
        return results
        
    # åä¸ªåæ°éè¦éå½ä¼ é
    #   results
    #   result ={}
    #   s
    #   startIndex

    def Helper(self, results, result, s, startIndex):
        if startIndex == len(s):
            results.append(result[:]) 
            return 
        #result.append(subset) only copy the reference of the subset, it will be changed with the change of subset
        
        for i in range(startIndex, len(s)):
            if self.isPalindrome(s[startIndex:i + 1]):
                result.append(s[startIndex:i + 1])
                self.Helper(results, result, s, i + 1)
                del result[-1] #subset=subset[:-1] doesn't work
    
    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True