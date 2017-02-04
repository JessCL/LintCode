# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/word-ladder-ii
@Language: Python
@Datetime: 17-01-02 04:54
'''

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def __init__(self):
        self.hash = {}
    
    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        if start == end:
            return 1
        length = self.BFS(start, end, dict)
        results = []
        self.DFS(start, end, dict, [end], results)
        return results
        
    def DFS(self, start, end, dict, result, results):
        if start == end:
            results.append(result[:])
            return
        
        for newWord in self.getNextWord(end, dict):
            if self.hash.has_key(newWord) and self.hash[newWord] == (self.hash[end] - 1):
                result = [newWord] + result
                self.DFS(start, newWord, dict, result, results)
                result = result[1:]
            
        
    def BFS(self, start, end, dict):
        queue = []
        queue.append(start)
        self.hash[start] = 0
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
                        self.hash[newWord] = self.hash[word] + 1
                        return length + 1
                    if newWord not in visited:
                        queue.append(newWord)
                        visited.add(newWord)
                        self.hash[newWord] = self.hash[word] + 1
                        
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