# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/two-sum
@Language: Python
@Datetime: 16-12-21 02:11
'''

class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        nums = [(0,0)] * len(numbers)
        for i in range(len(numbers)):
            nums[i] = (numbers[i], i)
        nums.sort()
        
        start = 0
        end = len(numbers) - 1
        while True:
            if nums[start][0] + nums[end][0] == target:
                if nums[start][1] > nums[end][1]:
                    return [nums[end][1] + 1, nums[start][1] + 1]
                else:
                    return [nums[start][1] + 1, nums[end][1] + 1]
            elif nums[start][0] + nums[end][0] < target:
                start += 1
            else:
                end -= 1   
        