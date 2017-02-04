# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/super-ugly-number
@Language: Python
@Datetime: 16-12-17 07:43
'''

class Solution:
    # @param {int} n a positive integer
    # @param {int[]} primes the given prime list
    # @return {int} the nth super ugly number
    def nthSuperUglyNumber(self, n, primes):
        k = len(primes)
        index = [0 for _ in range(k)]
        nextMultipleOf = primes[:]
        ugly = [0 for _ in range(n)]
        ugly[0] = 1
        for i in range(1,n):
            nextUglyNumber = sys.maxint
            for j in nextMultipleOf:
                if j < nextUglyNumber:
                    nextUglyNumber = j
            ugly[i] = nextUglyNumber
            for j in range(k):
                if nextMultipleOf[j] == nextUglyNumber:
                    index[j] += 1
                    nextMultipleOf[j] = ugly[index[j]] * primes[j]
        return ugly[-1]
        