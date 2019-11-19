class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic.keys():
                return [dic[complement], i]
            dic[nums[i]] = i
