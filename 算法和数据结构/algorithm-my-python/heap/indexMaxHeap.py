#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 8:52
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : indexMaxHeap.py
# @Software: PyCharm
import random


class IndexMaxHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = [0] * (capacity + 1)
        self.reverse = [0] * (capacity + 1)
        self.data = [0] * (capacity + 1)
        self.count = 0

    def __sizeof__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    # 插入一个元素到堆中，使用shift_up维持最大堆的特性
    # 对传入i的用户而言，是从0开始索引的
    def insert(self, i, item):
        assert self.count + 1 <= self.capacity
        assert 1 <= i + 1 <= self.capacity

        i += 1
        self.data[i] = item
        self.index[self.count + 1] = i
        self.reverse[i] = self.count + 1

        self.count += 1
        self.shift_up(self.count)

    def shift_up(self, k):
        while k > 1 and self.data[self.index[k // 2]] < self.data[self.index[k]]:
            self.index[k // 2], self.index[k] = self.index[k], self.index[k // 2]
            self.reverse[self.index[k // 2]] = k // 2
            self.reverse[self.index[k]] = k
            k = k // 2

    # 取出堆顶的元素，使用shift_down维持最大堆的特性
    def extract_max(self):
        assert not self.is_empty()
        ret = self.data[self.index[1]]
        self.index[1], self.index[self.count] = self.index[self.count], self.index[1]
        self.reverse[self.index[i]] = 1
        self.reverse[self.index[self.count]] = 0
        self.count -= 1
        self.shift_down(1)
        return ret

    def shift_down(self, k):
        while 2 * k <= self.count:
            j = 2 * k
            if j + 1 <= self.count and self.data[self.index[j + 1]] > self.data[self.index[j]]:
                j += 1
            if self.data[self.index[k]] >= self.data[self.index[j]]:
                break
            self.index[k], self.index[j] = self.index[j], self.index[k]
            self.reverse[self.index[k]] = k
            self.reverse[self.index[j]] = j
            k = j

    # 返回堆顶点的值在原data列表中的索引
    def extract_max_index(self):
        assert not self.is_empty()
        ret = self.index[1] - 1
        self.index[1], self.index[self.count] = self.index[self.count], self.index[1]
        self.reverse[self.index[i]] = 1
        self.reverse[self.index[self.count]] = 0
        self.count -= 1
        self.shift_down(1)
        return ret

    # 返回索引i位置的值
    def get_item(self, i):
        assert self.contain(i)
        return self.data[i + 1]

    # 改变索引i位置的值为new_item
    def change(self, i, new_item):
        assert self.contain(i)
        i += 1
        self.data[i] = new_item

        # for i in range(1, self.count + 1):
        #     if self.index[j] == i:
        #         self.shift_up(j)
        #         self.shift_down(j)

        j = self.reverse[i]
        self.shift_up(j)
        self.shift_down(j)

    def contain(self, i):
        assert 1 <= i + 1 <= self.capacity
        return not self.reverse[i + 1] == 0

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    max_heap = IndexMaxHeap(100)
    for i in range(15):
        max_heap.insert(random.randint(1, 100))
    print(max_heap)
    while not max_heap.is_empty():
        print(max_heap.extract_max())
