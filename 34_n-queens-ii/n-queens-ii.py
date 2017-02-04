# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/n-queens-ii
@Language: Python
@Datetime: 16-12-22 22:30
'''

class Solution:
    """
    Calculate the total number of distinct N-Queen solutions.
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        results = []
        self.Helper(results, [] ,n)
        #return self.draw(results)
        return len(results)
        
    def Helper(self, results, result, n):
        if len(result) == n:
            results.append(result[:])
        for row in range(n):
            if row not in result and self.isValid(result, row): #and isValid
                result.append(row)
                self.Helper(results, result, n)
                del result[-1]
    def isValid(self, result, x1):
        y1 = len(result)
        for y2 in range(len(result)):
            x2 = result[y2]
            if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
                return False
        return True
    def draw(self, results):
        num = len(results)
        
        if num == 0:
            return []
        n = len(results[0])
        chess = [[["."]*n for _ in range(n)] for _ in range(num)]
        for i in range(num):
            for y in range(n):
                chess[i][results[i][y]][y] = "Q"
                chess[i][results[i][y]] ="".join(chess[i][results[i][y]])
        return chess
