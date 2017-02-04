# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/longest-common-subsequence
@Language: Python
@Datetime: 16-12-15 18:24
'''

class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        lenA = len(A)
        lenB = len(B)
        f = [[0 for _ in range(lenB + 1)] for _ in range(lenA + 1)]
        # f[i][j]è¡¨ç¤ºåiä¸ªå­ç¬¦éä¸åjä¸ªå­ç¬¦çLCSçé¿åº¦
        for i in range(1, lenA + 1):
            for j in range(1, lenB + 1):
                f[i][j] = max(f[i-1][j],f[i][j-1])
                if A[i-1] == B[j-1]:
                    f[i][j] = max(f[i][j], f[i-1][j-1] + 1)
        #print f
        return f[-1][-1]
            
