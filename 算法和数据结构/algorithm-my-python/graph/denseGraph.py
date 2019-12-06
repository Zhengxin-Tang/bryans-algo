#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 19:44
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : denseGraph.py
# @Software: PyCharm
from graph.edge import *


class DenseGraph:
    def __init__(self, n, directed):
        self.n = n  # 点的数量
        self.m = 0  # 边的数量
        self.directed = directed
        self.matrix = [[None for i in range(n)] for i in range(n)]

    def V(self):
        return self.n

    def E(self):
        return self.m

    def add_edge(self, v, w, weight):
        assert (0 <= v < self.n)
        assert (0 <= w < self.n)
        if self.has_edge(v, w):
            del self.matrix[v][w]
            if not self.directed:
                del self.matrix[w][w]
            self.m -= 1
            self.matrix[v][w] = Edge(v, w, weight)

        if not self.directed:
            self.matrix[w][v] = Edge(v, w, weight)
        self.m += 1

    def has_edge(self, v, w):
        assert (0 <= v < self.n)
        assert (0 <= w < self.n)
        return self.matrix[v][w] is not None


if __name__ == '__main__':
    matrix = [[False for i in range(4)] for i in range(4)]
    print(matrix)