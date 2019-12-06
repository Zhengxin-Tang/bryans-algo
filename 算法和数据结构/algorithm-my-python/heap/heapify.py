#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 20:52
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : heapify.py
# @Software: PyCharm
import random


# 与maxHeap的构造方法不同，是直接传入一个数组并直接建成最大堆，算法复杂度O(n)
class Heapify:
    def __init__(self, arr):
        n = len(arr)
        self.data = [0] * (n + 1)
        self.capacity = n
        for i in range(n):
            self.data[i + 1] = arr[i]
        self.count = n

        # 算法复杂度的差别主要来自这里  或者可以对所有叶子节点进行一次shift_up?
        # for i in range(self.count//2, 0, -1):
        #     self.shift_down(i)

        # for i in range(self.count//2 + 1, self.count + 1):
        #     self.shift_up(i)

        for i in range(self.count, self.count//2, -1):
            self.shift_up(i)


    def __sizeof__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def insert(self, item):
        assert self.count + 1 <= self.capacity
        self.data[self.count + 1] = item
        self.count += 1
        self.shift_up(self.count)

    def shift_up(self, k):
        while k > 1 and self.data[k // 2] < self.data[k]:
            self.data[k // 2], self.data[k] = self.data[k], self.data[k // 2]
            k = k // 2

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
    a = []
    for i in range(15):
        a.append(random.randint(1, 100))
    max_heap = Heapify(a)
    print(max_heap)
    while not max_heap.is_empty():
        print(max_heap.extract_max())

