# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/hash-function
@Language: Python
@Datetime: 16-12-29 02:43
'''

class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        sum = 0
        for x in key:
            sum = (sum * 33 + ord(x)) % HASH_SIZE
        return sum 