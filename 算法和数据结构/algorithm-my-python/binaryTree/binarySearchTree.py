#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 10:20
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : binarySearchTree.py
# @Software: PyCharm
import queue


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def insert(self, key, value):
        self.root = self.insert_node(self.root, key, value)

    # 向树中插入一个node
    def insert_node(self, node, key, value):
        if not node:
            self.count += 1
            return Node(key, value)
        if key == node.key:
            node.value == value
        elif key < node.key:
            node.left = self.insert_node(node.left, key, value)
        else:
            node.right = self.insert_node(node.right, key, value)

    # 树中是否包含这个key
    def contain(self, key):
        return self.contain_node(self.root, key)

    def contain_node(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self.contain_node(node.left, key)
        else:
            return self.contain_node(node.right, key)

    # 搜索Key对应的value
    def search(self, key):
        return self.search_key(self.root, key)

    def search_key(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self.search_key(node.left, key)
        else:
            return self.search_key(node.right, key)

    # 前序优先遍历
    def pre_order(self):
        self.pre_order_node(self.root)

    def pre_order_node(self, node):
        if node:
            print(node.value)
            self.pre_order_node(node.left)
            self.pre_order_node(node.right)

    # 中序优先遍历
    def in_order(self):
        self.in_order_node(self.root)

    def in_order_node(self, node):
        if node:
            self.in_order_node(node.left)
            print(node.value)
            self.pre_order_node(node.right)

    # 后序优先遍历
    def post_order(self):
        self.post_order_node(self.root)

    def post_order_node(self, node):
        if node:
            self.post_order_node(node.left)
            self.post_order_node(node.right)
            print(node.value)

    # 广度优先搜索， 使用队列
    def level_order(self):
        q = queue.Queue(maxsize=self.count)
        q.put(self.root)
        while not q.empty():
            node = q.get()
            print(node.key)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

    # 寻找最小的key
    def minimum_node(self):
        assert not self.count == 0
        min_node = self.minimum_node_key(self.root)
        return min_node.key

    def minimum_node_key(self, node):
        if node.left is None:
            return node
        return self.minimum_node_key(node.left)

    # 寻找最大的key
    def maximum_node(self):
        assert not self.count == 0
        max_node = self.maximum_node_key(self.root)
        return max_node.key

    def maximum_node_key(self, node):
        if node.right is None:
            return node
        return self.maximum_node_key(node.right)

    # 删除最小值所在的节点
    def remove_min(self):
        if self.root is not None:
            self.root = self.remove_min_node(self.root)

    def remove_min_node(self, node):
        if node.left is None:
            right_node = node.right
            del node
            self.count -= 1
            return right_node
        node.left = self.remove_min_node(node.left)
        return node

    # 删除最大值所在的节点
    def remove_max(self):
        if self.root is not None:
            self.root = self.remove_max_node(self.root)

    def remove_max_node(self, node):
        if node.right is None:
            left_node = node.left
            del node
            self.count -= 1
            return left_node
        node.right = self.remove_max_node(node.right)
        return node

    # 删除键值为Key的节点
    def remove(self, key):
        self.root = self.remove_key(self.root, key)

    def remove_key(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self.remove_key(node.left, key)
            return node
        elif key > node.key:
            node.right = self.remove_key(node.right, key)
            return node
        else:
            if node.left is None:
                right_node = node.right
                del node
                self.count -= 1
                return right_node
            if node.right is None:
                left_node = node.left
                del node
                self.count -= 1
                return left_node
            # 左右孩子都不为空的情况
            successor = Node(self.minimum_node_key(node.right).key, self.minimum_node_key(node.right).value)
            self.count += 1
            # 这里可不可以直接用node.right?
            successor.right = self.remove_min_node(node.right)
            successor.left = node.left
            del node
            self.count -= 1
            return successor
