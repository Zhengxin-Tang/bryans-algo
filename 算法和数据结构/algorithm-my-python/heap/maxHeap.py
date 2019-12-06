#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 18:05
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : maxHeap.py
# @Software: PyCharm
import random


class MaxHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [0] * (capacity + 1)
        self.count = 0

    def __sizeof__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    # 插入一个元素到堆中，使用shift_up维持最大堆的特性
    def insert(self, item):
        assert self.count + 1 <= self.capacity
        self.data[self.count + 1] = item
        self.count += 1
        self.shift_up(self.count)

    def shift_up(self, k):
        while k > 1 and self.data[k // 2] < self.data[k]:
            self.data[k // 2], self.data[k] = self.data[k], self.data[k // 2]
            k = k // 2

    # 取出堆顶的元素，使用shift_down维持最大堆的特性
    def extract_max(self):
        assert not self.is_empty()
        ret = self.data[1]
        self.data[1], self.data[self.count] = self.data[self.count], self.data[1]
        self.count -= 1
        self.shift_down(1)
        return ret

    def shift_down(self, k):
        while 2 * k <= self.count:
            j = 2 * k
            if j + 1 <= self.count and self.data[j + 1] > self.data[j]:
                j += 1
            if self.data[k] >= self.data[j]:
                break
            self.data[k], self.data[j] = self.data[j], self.data[k]
            k = j

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    max_heap = MaxHeap(100)
    for i in range(15):
        max_heap.insert(random.randint(1, 100))
    print(max_heap)
    while not max_heap.is_empty():
        print(max_heap.extract_max())
