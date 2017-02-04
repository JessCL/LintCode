# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/top-k-largest-numbers
@Language: Python
@Datetime: 16-12-17 22:20
'''


class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
    def topk(self, nums, k):
        # k size min-heap
        # 1. build initial heap
        # n number of given nums
        n = len(nums)
        if n <= k:
            return sorted(nums, reverse = True)  # sortedä¸å½±åæ¬èº«ç»æ
        heap = [0] * (k + 1)
        # heap[0]: sizeOfHeap
        # getFather i/2 ; getLeftChild: i*2; getRightChild: i*2+1
        for i in range(k):
            self.hPush(heap, nums[i])
        # print heap
        for i in range(k, n):
            if nums[i] > self.hPeek(heap):
                self.hSiftDown(heap, nums[i])
            # print heap
        return sorted(heap[1:], reverse = True)
        
    def hPush(self, heap, target):
        heap[0] += 1
        curtIdx = heap[0]
        heap[curtIdx] = target
        # siftup
        while curtIdx / 2 >= 1 and heap[curtIdx / 2] > heap[curtIdx]:
            swap = heap[curtIdx]
            heap[curtIdx] = heap[curtIdx / 2]
            heap[curtIdx / 2] = swap
            curtIdx = curtIdx / 2
            
    def hPeek(self, heap):
        return heap[1]
        
    def hSiftDown(self, heap, target):
        heap[1] = target
        curtIdx = 1
        while True:
            leftIdx = curtIdx * 2
            rightIdx = curtIdx * 2 + 1
            if rightIdx <= heap[0] and heap[leftIdx] < heap[curtIdx] and heap[rightIdx] < heap[curtIdx]:
                if heap[leftIdx] < heap[rightIdx]:
                    swap = heap[curtIdx]
                    heap[curtIdx] = heap[leftIdx]
                    heap[leftIdx] = swap
                    curtIdx = leftIdx
                else:
                    swap = heap[curtIdx]
                    heap[curtIdx] = heap[rightIdx]
                    heap[rightIdx] = swap
                    curtIdx = rightIdx
            elif leftIdx <= heap[0] and heap[leftIdx] < heap[curtIdx]:
                swap = heap[curtIdx]
                heap[curtIdx] = heap[leftIdx]
                heap[leftIdx] = swap
                curtIdx = leftIdx
            elif rightIdx <= heap[0] and heap[rightIdx] < heap[curtIdx]:
                swap = heap[curtIdx]
                heap[curtIdx] = heap[rightIdx]
                heap[rightIdx] = swap
                curtIdx = rightIdx
            else:
                break