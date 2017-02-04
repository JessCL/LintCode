# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/top-k-frequent-words
@Language: Python
@Datetime: 16-12-18 01:07
'''

from heapq import *
class Solution:
    # @param {string[]} words a list of string
    # @param {int} k an integer
    # @return {string[]} a list of string
    def topKFrequentWords(self, words, k):
        if k == 0:
            return []
        dict = {}
        temp = []
        sizeOfHeap = 0
        for word in words:
            if dict.has_key(word):
                dict[word] -= 1
            else:
                dict[word] = -1
        for word in dict:
            temp.append((dict[word], word))
        temp.sort()
        result = [""] * k
        for index, (freq, word) in enumerate(temp):
            if index < k:
                result[index] = word
            else:
                break
        return result
        
        