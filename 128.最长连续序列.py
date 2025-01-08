#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 朴素解法：对数组进行排序，再进行连续性判断
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)
        # 默认为 1，因为当前数字也需要包含在内
        res = -float('inf')
        temp = 0
        for index, num in enumerate(sorted_nums):
            # 后方 = 当前 + 1, 计数 + 1，继续遍历
            if index == 0 or sorted_nums[index] == sorted_nums[index - 1] + 1:
                temp += 1
            elif sorted_nums[index] == sorted_nums[index - 1]:
                continue
            # 否则重新计数
            else:
                if res < temp:
                    res = temp
                temp = 1
        # 考虑全部都是连续的情况，res没有被赋值
        return max(res, temp)
# @lc code=end

