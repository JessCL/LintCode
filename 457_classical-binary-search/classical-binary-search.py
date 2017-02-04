# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/classical-binary-search
@Language: Python
@Datetime: 16-10-29 04:07
'''

class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        # Write your code here
        if len(A) == 0:
            return -1
        start = 0
        end = len(A) - 1
        while start + 1 < end:  #å¦æç¸é»å°±éåºï¼æéåï¼ä¸å¼å§åªæä¸ä¸ªåç´ çæåµï¼
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1