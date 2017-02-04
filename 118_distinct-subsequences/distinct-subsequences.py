# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/distinct-subsequences
@Language: Python
@Datetime: 16-12-15 18:53
'''

class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        #f[i][j] è¡¨ç¤º Sçåiä¸ªå­ç¬¦ä¸­éåTçåjä¸ªå­ç¬¦,æå¤å°ç§æ¹æ¡
        lenS = len(S)
        lenT = len(T)
        f = [[0 for _ in range(lenT + 1)] for _ in range(lenS + 1)]
        for i in range(lenS + 1):
            f[i][0] = 1
        for i in range(1, lenS + 1):
            for j in range(1, lenT + 1):
                if S[i-1] == T[j-1]:
                    f[i][j] = f[i-1][j-1] + f[i-1][j]
                else:
                    f[i][j] = f[i-1][j]
        return f[-1][-1]
                