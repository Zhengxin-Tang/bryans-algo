#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 22:51
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : bubbleSort.py
# @Software: PyCharm


def bubble_sort(arr):
    exchange = False
    n = len(arr)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                exchange = True
        if not exchange:
            break


if __name__ == '__main__':
    a = [1,2,3,5,4,6,7,8,9]
    bubble_sort(a)
    print(a)
