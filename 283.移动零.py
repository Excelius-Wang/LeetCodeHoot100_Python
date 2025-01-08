#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        思路：
        利用双指针, 前一个指针标记0, 后一个指针标记非0元素。
        从前往后遍历, 前指针遇到了0, 后指针就找第一个非0元素进行交换, 直到前指针遍历完。
        """
        if nums == None:
            return
        j = 0
        for index, num in enumerate(nums):
            # 当 index 指向的数据不为 0 时, 就和 j 指向的数进行交换
            if num != 0:
                temp = num
                nums[index] = nums[j]
                nums[j] = temp
                j += 1
# @lc code=end

