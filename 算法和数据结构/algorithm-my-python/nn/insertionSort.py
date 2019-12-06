#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 21:30
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : insertionSort.py
# @Software: PyCharm
from nn.selectionSort import *


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j = i
        while j > 0 and arr[j-1] > current:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = current


if __name__ == '__main__':
    n = 10000
    random_list1 = generate_nearly_ordered_array(n, 10)
    random_list2 = copy_array(random_list1)
    test_sort("Selection sort: ", selection_sort, random_list1)
    test_sort("Insertion sort: ", insertion_sort, random_list2)


