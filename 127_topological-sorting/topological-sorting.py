# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/topological-sorting
@Language: Python
@Datetime: 16-11-27 05:47
'''

# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        queue = []
        inDegree = {}
        for node in graph:
            inDegree[node] = 0
        for node in graph:
            for nb in node.neighbors:
                inDegree[nb] += 1
        for node in graph:
            if inDegree[node] == 0:
                queue.append(node)
        result = []
        while len(queue) != 0:
            current = queue[0]
            del queue[0]
            result.append(current)
            for nb in current.neighbors:
                inDegree[nb] -= 1
                if inDegree[nb] == 0:
                    queue.append(nb)
        return result  