# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/six-degrees
@Language: Python
@Datetime: 17-01-02 00:38
'''

# Definition for Undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    '''
    @param {UndirectedGraphNode[]} graph a list of Undirected graph node
    @param {UndirectedGraphNode} s, t two Undirected graph nodes
    @return {int} an integer
    '''
    def sixDegrees(self, graph, s, t):
        # Write your code here
        if s == t:
            return 0
        queue = []
        queue.append(s)
        visited = set()
        visited.add(s)
        degree = 0
        while len(queue) > 0:
            size = len(queue)
            degree += 1
            for i in range(size):
                current = queue[0]
                del queue[0]
                for neighbor in current.neighbors:
                    if neighbor == t:
                        return degree
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        return -1
                        