#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 20:44
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : heapSort1.py
# @Software: PyCharm
from heap.maxHeap import *


# 先将n个元素逐个插入到一个空堆中，然后再反向取出堆元素
# 缺点一个是算法复杂度是O(nlogn)比heapify要高，另一个是空间上，多使用了一个数组的空间
def heap_sort1(arr):
    n = len(arr)
    max_heap = MaxHeap(n)
    for i in range(n):
        max_heap.insert(arr[i])
    for i in range(n - 1, -1, -1):
        arr[i] = max_heap.extract_max()


if __name__ == '__main__':
    a = [1, 4, 2, 3, 7, 5, 9, 8, 10, 6]
    heap_sort1(a)
    print(a)
