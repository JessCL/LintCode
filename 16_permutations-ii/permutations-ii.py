# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/permutations-ii
@Language: Python
@Datetime: 16-11-27 06:58
'''

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        results = []
        nums.sort()
        visited = [0 for _ in nums]
        self.Helper(results, [], nums, visited)
        return results
        
    def Helper(self, results, curRes, nums, visited):
        if len(curRes) == len(nums):
            results.append(curRes[:])
            return
        
        for i in range(len(nums)):
            if visited[i] == 1 or ( i != 0 and nums[i] == nums[i-1] and visited[i-1] == 0):
                continue
            curRes.append(nums[i])
            visited[i] = 1
            self.Helper(results, curRes, nums, visited)
            del curRes[-1]
            visited[i] = 0
                