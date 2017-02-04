# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/connected-component-in-undirected-graph
@Language: Python
@Datetime: 17-01-02 01:08
'''

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        queue = []
        visited = set()
        result = []
        results = []
        i = -1
        
        while True:
            while i < len(nodes) - 1:
                i += 1
                if nodes[i] not in visited:
                    queue.append(nodes[i])
                    visited.add(nodes[i])
                    break
            else:
                return results
                
            while len(queue) > 0:
                current = queue[0]
                del queue[0]
                result.append(current.label)
                for neighbor in current.neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            result.sort()
            results.append(result)
            result = []