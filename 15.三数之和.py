#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        # 先排序, 这样我们可以得到三个数字的下标一定会满足 k < i < j
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            # 除非都为 0, 否则必须要有 < 0 的数字
            if nums[k] > 0:
                break

            # 跳过相同的 k 值
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            # i 从 k + 1 开始, j 从最右边开始; 即 一左一右
            i, j = k + 1, len(nums) - 1

            # 双指针找 i 和 j
            while i < j:
                # 计算和值 s
                s = nums[k] + nums[i] + nums[j]
                # 如果 s < 0, 说明和值需要增大, 只有 i 向右走才会变大（j 只往左走）
                if s < 0:
                    i += 1
                    # 如果遇到了相同的值, 则继续跳过
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                # 如果 s > 0, 说明值需要减小, j 需要往左走
                elif s > 0:
                    j -= 1
                    # 跳过相同的值
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    # 刚好为 0, 加入到 结果中
                    res.append([nums[k], nums[i], nums[j]])
                    # i, j 继续移动, 同样跳过相同的值
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res
# @lc code=end
