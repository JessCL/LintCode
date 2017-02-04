# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/word-ladder
@Language: Python
@Datetime: 16-12-23 18:46
'''

'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
'''        
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        if start == end:
            return 1
        return self.BFS(start, end, dict)
        
    def BFS(self, start, end, dict):
        queue = []
        queue.append(start)
        visited = set()
        visited.add(start)
        length = 0
        while len(queue) > 0:
            size = len(queue)
            length += 1
            for i in xrange(size):
                word = queue[0]
                del queue[0]
                for newWord in self.getNextWord(word, dict):
                    if newWord == end:
                        return length + 1
                    if newWord not in visited:
                        queue.append(newWord)
                        visited.add(newWord)
                        
    def getNextWord(self, word, dict):
        wordList = []
        for i in xrange(len(word)):# å¯¹æ¯ä¸ªå­ç¬¦
            part1 = word[:i]; part2 = word[i+1:]
            for ch in "abcdefghijklmnopqrstuvwxyz":   #25ç§åæ¢å¯è½æ§
                if ch != word[i]:
                    newWord = part1 + ch + part2
                    if newWord in dict:
                        wordList.append(newWord)
        return wordList
        
                    