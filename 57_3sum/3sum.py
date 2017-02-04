# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/3sum
@Language: Python
@Datetime: 16-12-21 19:46
'''

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        numbers.sort()
        #print numbers
        results = []
        
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            target = - numbers[i]
            
            start = i + 1
            end = len(numbers) - 1
            
            while start < end:
                if numbers[start] + numbers[end] < target:
                    start += 1
                elif numbers[start] + numbers[end] > target:
                    end -= 1
                else: #  numbers[start] + numbers[end] == target
                    result = [- target, numbers[start], numbers[end]]
                    result.sort()
                    result = tuple(result)
                    results.append(result)
                    start += 1
                    end -= 1
                    while start < len(numbers) and numbers[start] == numbers[start - 1]:
                        start += 1
                    while end > 0 and numbers[end] == numbers[end + 1]:
                        end -= 1
        if len(results) > 0:
            results.sort()
        return results
            
        