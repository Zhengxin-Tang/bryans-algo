#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 16:44
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : unionFind2.py
# @Software: PyCharm


# quick union
class UnionFind:
    def __init__(self, n):
        self.count = n
        # sz[i]表示以i为跟的集合中元素的个数
        self.sz = [0] * n
        self.parent = [0] * n
        for i in range(n):
            self.parent[i] = i
            self.sz[i] = i

    # 找到p是属于那个集的
    def find(self, p):
        assert 0 <= p <= self.count
        while not p == self.parent[p]:
            p == self.parent[p]
        return p

    # p和q是否属于同一个集
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union_elements(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if not p_root == q_root:
            if self.sz[p_root] < self.sz[q_root]:
                self.parent[p_root] == q_root
                self.sz[q_root] += self.sz[p_root]
            else:
                self.parent[q_root] = p_root
                self.sz[p_root] += self.sz[q_root]
