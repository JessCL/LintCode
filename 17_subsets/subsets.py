# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/subsets
@Language: Python
@Datetime: 16-10-24 06:22
'''

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        S.sort() #elements in a subset must be in non-descending order
        result = []
        self.subsetsHelper(result, [], S, 0)
        return result

    def subsetsHelper(self, result, subset, S, startIndex):
        result.append(subset[:]) #result.append(subset) only copy the reference of the subset, it will be changed with the change of subset
        for i in range(startIndex, len(S)):
            subset.append(S[i])
            self.subsetsHelper(result, subset, S, i + 1)
            del subset[-1] #subset=subset[:-1] doesn't work
        