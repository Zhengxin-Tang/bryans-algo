#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 21:33
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : heapSort2.py
# @Software: PyCharm
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 20:44
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : heapSort1.py
# @Software: PyCharm
from heap.heapify import *


# 使用heapify直接构造了一个最大堆，然后直接反向取出堆元素
# 省去了将n个元素逐个插入到空堆的过程
def heap_sort2(arr):
    n = len(arr)
    heapify = Heapify(arr)
    for i in range(n - 1, -1, -1):
        arr[i] = heapify.extract_max()


if __name__ == '__main__':
    b = [1, 4, 2, 3, 7, 5, 9, 8, 10, 6]
    heap_sort2(b)
    print(b)
