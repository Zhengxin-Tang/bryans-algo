#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 19:49
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : Student.py
# @Software: PyCharm


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __gt__(self, other):
        if self.score > other.score:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.score < other.score:
            return True
        else:
            return False

    def __str__(self):
        return str(self.name) + ": " + str(self.score)
