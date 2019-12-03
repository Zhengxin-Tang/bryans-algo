# 包含min函数的栈

定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

Python:
```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.assist = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.assist:
            self.assist.append(node)
        else:
            self.assist.append(min(node, self.assist[-1]))
    def pop(self):
        # write code here
        if not self.stack:
            return None
        self.assist.pop()
        return self.stack.pop()
    def top(self):
        # write code here
        if not self.stack:
            return None
        return self.stack[-1]
    def min(self):
        # write code here
        if not self.assist:
            return None
        return self.assist[-1]
```
