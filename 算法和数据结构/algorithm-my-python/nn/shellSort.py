#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 10:24
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : shellSort.py
# @Software: PyCharm


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for start_position in range(gap):
            gap_insertion_sort(arr, start_position, gap)
        gap = gap // 2


def gap_insertion_sort(arr, start_position, gap):
    n = len(arr)
    for i in range(start_position + gap, n, gap):
        current = arr[i]
        j = i
        while j > start_position and arr[j - gap] > current:
            arr[j] = arr[j - gap]
            j -= gap
        arr[j] = current


if __name__ == '__main__':
    a = [6, 4, 5, 1, 1, 1, 2, 2, 3, 4, 4, 4, 8, 9, 7]
    shell_sort(a)
    print(a)
