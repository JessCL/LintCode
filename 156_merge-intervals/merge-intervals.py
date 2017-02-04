# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/merge-intervals
@Language: Python
@Datetime: 16-11-13 07:07
'''



"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
   
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        # write your code here
        if len(intervals) <= 1:
            return intervals
        def byStart_key(interval):
            return interval.start
        intervals.sort(key = byStart_key)
        prev = intervals[0]
        result = []
        for i in range(1, len(intervals)):
            curt = intervals[i]
            if min(prev.end, curt.end) - curt.start >= 0:
                prev = Interval(prev.start, max(prev.end, curt.end))
            else:
                result.append(prev)
                prev = curt
        result.append(prev)      
        return result