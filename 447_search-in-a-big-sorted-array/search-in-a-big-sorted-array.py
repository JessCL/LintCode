# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/search-in-a-big-sorted-array
@Language: Python
@Datetime: 16-11-02 03:22
'''

"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 if index is less than zero.
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader 
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        if reader.get(0) == target:
            return 0
        end = 1
        while reader.get(end) < target:
            end *= 2
            
        start = end / 2 + 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if reader.get(mid) == target:
                end = mid
            elif reader.get(mid) < target:
                start = mid
            else:
                end = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
        