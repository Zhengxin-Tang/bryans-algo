#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 20:17
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : SortTestHelper.py
# @Software: PyCharm

import random
import time


def generate_random_array(n, range_l, range_r):
    random_list = [0]*n
    for i in range(n):
        random_list[i] = random.randint(range_l,range_r)
    return random_list


def generate_nearly_ordered_array(n, swap_times):
    nearly_ordered_list = [0] * n
    for i in range(n):
        nearly_ordered_list[i] = i
    for i in range(swap_times):
        posx = random.randint(0, n - 1)
        posy = random.randint(0, n - 1)
        nearly_ordered_list[posx], nearly_ordered_list[posy] = nearly_ordered_list[posy], nearly_ordered_list[posx]
    return nearly_ordered_list


def test_sort(sort_name, func, arr):
    t1 = time.time()
    func(arr)
    t2 = time.time()
    # assert is_sorted(arr)
    print(sort_name + str(t2 - t1))


def is_sorted(alist):
    n = len(alist)
    for i in range(n - 1):
        if alist[i] > alist[i + 1]:
            return False
    return True


def copy_array(arr):
    n = len(arr)
    new_list = [0]*n
    for i in range(n):
        new_list[i] = arr[i]
    return new_list
