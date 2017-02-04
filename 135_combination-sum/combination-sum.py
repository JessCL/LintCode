# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/combination-sum
@Language: Python
@Datetime: 16-12-22 22:40
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        results = []
        candidates = set(candidates)
        candidates = list(candidates)
        candidates.sort()
        self.Helper(results, [], candidates, target, 0)
        return results
    def Helper(self, results, result, candidates, target, startIndex):
        if target == 0:
            results.append(result[:])
            return
        for i in range(startIndex, len(candidates)):
            if candidates[i] > target:
                break
            result.append(candidates[i])
            self.Helper(results, result, candidates, target - candidates[i], i)
            del result[-1]
            