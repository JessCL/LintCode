# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/permutations
@Language: Python
@Datetime: 16-11-27 06:28
'''

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        results = []
        self.permuteHelper(results, [], nums)
        return results

    def permuteHelper(self, results, curRes, nums):
        
        if len(nums) == len(curRes):
            results.append(curRes[:])
            return

        for i in nums:
            if i not in curRes:
                curRes.append(i)
                self.permuteHelper(results, curRes, nums)
                del curRes[-1]
            
