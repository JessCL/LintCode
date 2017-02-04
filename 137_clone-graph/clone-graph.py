# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/clone-graph
@Language: Python
@Datetime: 16-11-27 06:04
'''

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}
    #DFS    
    def cloneGraph(self, node):
        queue = []
        visited = set()
        hashTable = {}
        if node is None:
            return None
        #copy all the nodes
        queue.append(node)
        visited.add(node)
        while len(queue) > 0:
            current = queue[0]
            del queue[0]
            newNode = UndirectedGraphNode(current.label)
            hashTable[current] = newNode
            for nb in current.neighbors:
                if nb not in visited:
                    queue.append(nb)
                    visited.add(nb)
        #copy all the edges
        queue.append(node)
        visited = set()
        visited.add(node)
        while len(queue) > 0:
            current = queue[0]
            del queue[0]
            newNode = hashTable[current]
            newNode.neighbors = []
            for nb in current.neighbors:
                newNode.neighbors.append(hashTable[nb])
                if nb not in visited:
                    queue.append(nb)
                    visited.add(nb)
        return hashTable[node]
            