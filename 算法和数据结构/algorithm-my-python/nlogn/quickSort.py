#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 12:14
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : quickSort.py
# @Software: PyCharm
from nn.SortTestHelper import *
from nlogn.mergeSort import *
import random


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)


def quick_sort_helper(arr, left, right):
    if left < right:
        # 优化1
        if right - left <= 16:
            insertion_sort(arr)
        p = partition(arr, left, right)
        quick_sort_helper(arr, left, p - 1)
        quick_sort_helper(arr, p + 1, right)


def partition(arr, left, right):
    # 优化2，解决近乎有序情况下的问题
    random_p = random.randint(left, right)
    arr[left], arr[random_p] = arr[random_p], arr[left]
    p = left
    for i in range(left + 1, right + 1):
        if arr[i] < arr[left]:
            arr[p + 1], arr[i] = arr[i], arr[p + 1]
            p += 1
    arr[left], arr[p] = arr[p], arr[left]
    return p


# 双路快排, 解决list中存在大量重复元素的问题
def quick_sort2(arr):
    quick_sort_helper2(arr, 0, len(arr) - 1)


def quick_sort_helper2(arr, left, right):
    if left < right:
        # 优化1
        if right - left <= 16:
            insertion_sort(arr)
        p = partition2(arr, left, right)
        quick_sort_helper2(arr, left, p - 1)
        quick_sort_helper2(arr, p + 1, right)


def partition2(arr, left ,right):
    random_p = random.randint(left, right)
    arr[left], arr[random_p] = arr[random_p], arr[left]
    i = left +1
    j = right
    while True:
        while i <= right and arr[i] < arr[left]:
            i += 1
        while j >= left + 1 and arr[j] > arr[left]:
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    arr[left], arr[j] = arr[j], arr[left]
    return j


#三路快排
def quick_sort3(arr):
    quick_sort_helper3(arr, 0, len(arr) - 1)


def quick_sort_helper3(arr, left, right):
    if left < right:
        # 优化1
        if right - left <= 16:
            insertion_sort(arr)
        # partition
        random_p = random.randint(left, right)
        arr[left], arr[random_p] = arr[random_p], arr[left]
        lt = left
        gt = right + 1
        i = left + 1
        while i < gt:
            if arr[i] < arr[left]:
                arr[i], arr[lt + 1] = arr[lt + 1] , arr[i]
                lt += 1
                i += 1
            elif arr[i] > arr[left]:
                arr[i], arr[gt - 1] = arr[gt - 1], arr[i]
                gt -= 1
            else:
                i += 1
        arr[left], arr[lt] = arr[lt], arr[left]
        quick_sort_helper3(arr, left, lt - 1)
        quick_sort_helper3(arr, gt, right)


if __name__ == '__main__':
    n = 5000
    random_list1 = generate_random_array(n, 0, 100000)
    random_list2 = copy_array(random_list1)
    random_list3 = copy_array(random_list1)
    random_list4 = copy_array(random_list1)
    random_list5 = copy_array(random_list1)
    test_sort("Insertion Sort: ", insertion_sort, random_list1)
    test_sort("Merge sort: ", merge_sort, random_list2)
    test_sort("Quick sort: ", quick_sort, random_list3)
    test_sort("Quick sort2: ", quick_sort2, random_list4)
    test_sort("Quick sort3: ", quick_sort3, random_list5)

    print("")

    random_list1 = generate_nearly_ordered_array(n, 100)
    random_list2 = copy_array(random_list1)
    random_list3 = copy_array(random_list1)
    random_list4 = copy_array(random_list1)
    random_list5 = copy_array(random_list1)
    test_sort("Insertion Sort: ", insertion_sort, random_list1)
    test_sort("Merge sort: ", merge_sort, random_list2)
    test_sort("Quick sort: ", quick_sort, random_list3)
    test_sort("Quick sort2: ", quick_sort2, random_list4)
    test_sort("Quick sort3: ", quick_sort3, random_list5)

    print("")

    random_list1 = generate_random_array(n, 0, 100)
    random_list2 = copy_array(random_list1)
    random_list3 = copy_array(random_list1)
    random_list4 = copy_array(random_list1)
    random_list5 = copy_array(random_list1)
    test_sort("Insertion Sort: ", insertion_sort, random_list1)
    test_sort("Merge sort: ", merge_sort, random_list2)
    test_sort("Quick sort: ", quick_sort, random_list3)
    test_sort("Quick sort2: ", quick_sort2, random_list4)
    test_sort("Quick sort3: ", quick_sort3, random_list5)

