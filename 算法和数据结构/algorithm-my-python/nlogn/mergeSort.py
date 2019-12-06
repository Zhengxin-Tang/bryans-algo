#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 10:51
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : mergeSort.py
# @Software: PyCharm
from nn.insertionSort import *


def merge_sort(arr):
    if len(arr) <= 16:
        # 优化2
        insertion_sort(arr)
    else:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        # 优化1
        if left_arr[-1] > right_arr[0]:
            merge(arr, left_arr, right_arr)


def merge(arr, left_arr, right_arr):
    i, j, k = 0, 0, 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        k += 1
        i += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        k += 1
        j += 1


if __name__ == '__main__':
    a = [6, 4, 5, 10, 1, 2, 3, 8, 9, 7]
    merge_sort(a)
    print(a)
