# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/data-stream-median
@Language: Python
@Datetime: 16-12-20 05:48
'''

from heapq import *
class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    # å¦ææ¯å¶æ°ä¸ªï¼ä¸­ä½æ°æ¯ä¸­é´ä¸¤ä¸ªé åçé£ä¸ªæ°
    def medianII(self, nums):
        minHeap = []
        maxHeap = []
        result = [0]* len(nums)
        for i in range(len(nums)):
            if len(maxHeap) == 0 or nums[i] <= -maxHeap[0]:
                heappush(maxHeap, - nums[i])
            else:
                heappush(minHeap, nums[i])
            
            if len(maxHeap) == len(minHeap):
                result[i] = - maxHeap[0]
            elif len(maxHeap) == len(minHeap) + 1:
                result[i] = - maxHeap[0]
            elif len(maxHeap) + 1 == len(minHeap):
                result[i] = minHeap[0]
            elif len(maxHeap) == len(minHeap) + 2:
                heappush(minHeap, - heappop(maxHeap))
                result[i] = - maxHeap[0]
            elif len(maxHeap) + 2 == len(minHeap):
                heappush(maxHeap, - heappop(minHeap))
                result[i] = - maxHeap[0]
        return result
