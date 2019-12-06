#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 16:24
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : unionFind.py
# @Software: PyCharm


# quick find  O(1)
class UnionFind:
    def __init__(self, n):
        self.count = n
        self.id = [0] * n
        for i in range(n):
            self.id[i] = i

    # 找到p是属于那个集的
    def find(self, p):
        assert 0 <= p <= self.count
        return self.id[p]

    # p和q是否属于同一个集
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union_elements(self, p ,q):
        p_id = self.find(p)
        q_id = self.find(q)
        if not p_id == q_id:
            for i in range(self.count):
                if self.id[i] == p_id:
                    self.id[i] = q_id
