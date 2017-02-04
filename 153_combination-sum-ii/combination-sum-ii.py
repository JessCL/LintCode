# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/combination-sum-ii
@Language: Python
@Datetime: 16-12-22 22:46
'''

class Solution:    
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target): 
        results = []
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
            if i > startIndex and candidates[i] == candidates[i-1]:
                continue
            result.append(candidates[i])
            self.Helper(results, result, candidates, target - candidates[i], i + 1)
            del result[-1]