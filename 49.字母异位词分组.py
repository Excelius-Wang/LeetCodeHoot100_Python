#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 设置一个哈希表保存一些字母可能的字符串组合, 格式为: "aet":["eat", "tae"]
        # 遍历每个元素, 把该元素里的字母按照字母顺序排序, 看看是否在哈希表里, 如果在, 添加到指定位置;
        # 不在, 就把当前元素作为新的数据插入进去
        str_map = dict()
        for index, str in enumerate(strs):
            sorted_str = ''.join(sorted(str))
            if sorted_str in str_map:
                str_map[sorted_str].append(str)
            else:
                str_map[sorted_str] = [str]

        return list(str_map.values());
# @lc code=end

