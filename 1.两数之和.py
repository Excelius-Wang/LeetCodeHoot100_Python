#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 使用哈希表进行存储查找，如果差值在哈希表里，直接返回；
        # 如果不在，把当前数放入到哈希表中
        num_dict = dict()
        for index, num in enumerate(nums):
            temp = target - num
            if temp in num_dict.keys():
                return num_dict.get(temp), index;
            else:
                num_dict[num] = index
# @lc code=end

