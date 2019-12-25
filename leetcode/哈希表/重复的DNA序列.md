# 重复的DNA序列

所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找 DNA 分子中所有出现超过一次的 10 个字母长的序列（子串）。

 

**示例：**
```
输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC", "CCCCCAAAAA"]
```

Java:
```java
class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        if(s.length() <= 10)
            return new ArrayList<String>();
        
        Set<String> set = new HashSet<>();
        Set<String> res = new HashSet<>();

        int left = 0;
        int right = 9;
        while(right < s.length()){
            String temp = s.substring(left, right + 1);
            if(set.contains(temp)){
                res.add(temp);
            }else{
                set.add(temp);
            }
            left++;
            right++;
        }
        return new ArrayList<String>(res);
    }
}
```
