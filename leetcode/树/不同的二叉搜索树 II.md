# 不同的二叉搜索树 II

给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

**示例:**
```
输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
```
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：
```
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```
**思路：**
递归。

如果将 i 作为跟节点，那么 [1, i) 为 i 的左子树节点，(i, n] 为右子树节点。

问题就被拆分为两个子问题了：

- 求左子树的所有排列
- 求右子树的所有排列

Java:
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<TreeNode> generateTrees(int n) {
        if(n < 1)
            return new ArrayList<TreeNode>();
        return generateTrees(1, n);
    }

    private List<TreeNode> generateTrees(int start, int end){
        List<TreeNode> res = new ArrayList<>();
        if(start > end){
            res.add(null);
            return res;
        }
        for(int i = start; i<=end; i++){
            List<TreeNode> subLeftTree = generateTrees(start, i-1);
            List<TreeNode> subRightTree = generateTrees(i+1, end);
            for(TreeNode left:subLeftTree){
                for(TreeNode right: subRightTree){
                    TreeNode node = new TreeNode(i);
                    node.left = left;
                    node.right = right;
                    res.add(node);
                }
            }
        }
        return res;
    }
}
```
