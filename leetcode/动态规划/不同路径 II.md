# 不同路径 II

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:
```
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
```
**解释:**
```
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
```
**思路：**
动态规划
- dp[i][j]表示到i-1行j-1列到位置一共有多少种路径
- 若nums[i][j]为1，dp[i][j] = 0
- 因为有障碍物到存在，把dp数组到初始值也放在训练中比较好，i==0和j==0时到情况也放在循环中判断，不能直接初始化为1
- dp[m-1][n-1]即为所求

Java:
```java
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if(obstacleGrid.length == 0 || obstacleGrid[0].length == 0)
            return 0;
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[][] dp = new int[m][n];
        for(int i = 0; i<m ; i++){
            for(int j = 0; j < n; j++){
                if(obstacleGrid[i][j] == 1){
                    dp[i][j] = 0;
                }else{
                    if(i == 0 & j == 0)
                        dp[i][j] = 1;
                    else if(i == 0)
                        dp[i][j] = dp[i][j-1];
                    else if(j == 0)
                        dp[i][j] = dp[i-1][j];
                    else
                        dp[i][j] = dp[i][j-1] + dp[i-1][j];
                }
            }
        }
        return dp[m-1][n-1];
    }
}
```
