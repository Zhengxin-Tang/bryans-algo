#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 19:59
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : edge.py
# @Software: PyCharm


class Edge:
    def __init__(self, a, b, weight):
        self.a = a
        self.b = b
        self.weight = weight

    def V(self):
        return  self.a

    def W(self):
        return  self.b

    def wt(self):
        return self.weight

    def other(self, x):
        assert x == self.a or x == self.b
        if x == self.a:
            return self.b
        else:
            return self.a

    def __str__(self):
        return str(self.a) + " - " + str(self.b) + ": " + str(self.weight)

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __ge__(self, other):
        return self.weight >= other.weight


