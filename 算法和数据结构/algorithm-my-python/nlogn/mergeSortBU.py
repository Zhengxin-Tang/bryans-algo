#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 11:45
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : mergeSortBU.py
# @Software: PyCharm


def merge_sort_bu(arr):
    n = len(arr)
    size = 1
    while size < n:
        blist = arr[:]
        i = 0
        while i + size < n:
            if arr[i + size - 1] < arr[i + size]:  # 优化1。优化2方案放弃。
                i = i + size + size
                continue
            a, b, c = i, i + size, i
            while a < i + size and b < min(i + size + size, n):
                if blist[a] <= blist[b]:
                    arr[c] = blist[a]
                    a += 1
                else:
                    arr[c] = blist[b]
                    b += 1
                c += 1
            while a < i + size:
                arr[c] = blist[a]
                a += 1
                c += 1
            while b < min(i + size + size, n):
                arr[c] = blist[b]
                b += 1
                c += 1
            i += size + size
        size += size


if __name__ == '__main__':
    a = [6, 4, 5, 10, 1, 2, 3, 8, 9, 7]
    merge_sort_bu(a)
    print(a)
