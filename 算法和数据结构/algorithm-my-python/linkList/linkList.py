#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 11:05
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : linkList.py
# @Software: PyCharm


class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_link_list(arr):
    if arr is None:
        return None

    head = LinkNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = LinkNode(arr[i])
        current = current.next
    return head


def delete_link_list(head):
    current = head
    while current is not None:
        del_node = current
        current = current.next
        del del_node


def print_link_list(head):
    current = head
    while current is not None:
        print(str(current.val) + " -> ", end='')
        current = current.next
    print("None")


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    link_list = create_link_list(arr)
    print_link_list(link_list)
    delete_link_list(link_list)
    print_link_list(link_list)