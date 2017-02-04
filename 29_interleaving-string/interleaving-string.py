# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/interleaving-string
@Language: Python
@Datetime: 16-12-15 19:22
'''

class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        #  f[i][j]è¡¨ç¤ºs1çåiä¸ªå­ç¬¦ås2çåjä¸ªå­ç¬¦è½å¦äº¤æ¿ç»æs3çåi+jä¸ªå­ç¬¦
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if (len1 + len2) != len3:
            return False
        f = [[False] * (len2 + 1) for _ in range(len1 + 1)] 
        f[0][0] = True
        for j in range(1,len1 + 1):
            if s3[j-1] == s1[j-1]:
                f[j][0] = True
            else:
                break
        for k in range(1,len2 + 1):
            if s3[k-1] == s2[k-1]:
                f[0][k] = True
            else:
                break
        
        for j in range(1,len1 + 1):
            for k in range(1,len2 + 1):
                f[j][k] =  (s3[j+k-1] == s1[j-1] and f[j-1][k]) or (s3[j+k-1] == s2[k-1] and f[j][k-1])
                        
        return f[-1][-1]