#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 21:49
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : heapSort3.py
# @Software: PyCharm


# 原地堆排序
# 与heapify不同的是构建堆的数组的索引是从0开始的
def heap_sort3(arr):
    n = len(arr)
    # 先从第一个非叶子节点到根节点做一遍shiftdown使数组变成最大堆
    for i in range((n - 1) // 2, -1, -1):
        shift_down(arr, n, i)

    # 再依次把当前最大元素放到数组最后，每次交换后再进行一次shiftdown维持最大堆
    for i in range((n - 1), 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        shift_down(arr, i, 0)


def shift_down(arr, n, k):
    while (2 * k + 1) <= n:
        j = 2 * k + 1
        if j + 1 < n and arr[j + 1] > arr[j]:
            j += 1
        if arr[k] >= arr[j]:
            break
        arr[k], arr[j] = arr[j], arr[k]
        k = j
