# 搜索旋转排序数组 II

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

**示例 1:**
```
输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
```
**示例 2:**
```
输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
```

**思路：**
和搜索旋转数组类似，不过这次可能存在重复元素，就在期间进行一下去重。

Java:非递归的二分查找
```java
class Solution {
    public boolean search(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        while(low <= high){
            while(low < high && nums[low] == nums[low+1])
                low++;
            while(low < high && nums[high] == nums[high-1])
                high--;
            int mid = low + (high - low)/2;
            if(nums[mid] == target)
                return true;
            if(nums[mid] < nums[high]){
                if(nums[mid] < target && nums[high] >= target)
                    low = mid + 1;
                else
                    high = mid - 1;
            }
            else{
                if(nums[mid] > target && nums[low] <= target)
                    high = mid - 1;
                else
                    low = mid + 1;
            }
        }
        return false;
    }
}
```
