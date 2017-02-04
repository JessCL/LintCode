# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/longest-common-substring
@Language: Python
@Datetime: 16-12-15 19:40
'''

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        lenA = len(A)
        lenB = len(B)
        result = 0
        # f[i][j] åå«Açç¬¬iä¸ªå­ç¬¦ä¸Bçç¬¬jä¸ªå­ç¬¦çsubstringçé¿åº¦
        f = [[0 for _ in range(lenB + 1)] for _ in range(lenA + 1)]
        for i in range (1, lenA + 1):
            for j in range(1, lenB + 1):
                if A[i-1] == B[j-1]:
                    f[i][j] = f[i-1][j-1] + 1
                    if f[i][j] > result:
                        result = f[i][j]
        return result

                        
                