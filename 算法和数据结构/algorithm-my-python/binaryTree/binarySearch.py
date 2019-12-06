#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 10:07
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : binarySearch.py
# @Software: PyCharm


# 不能很好处理查找的元素存在大量重复的情况
def binary_search(arr, target):
    n = len(arr)
    l = 0
    r = n - 1
    while l <= r:
        # mid = (l + r) // 2  可能会产生溢出
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1
