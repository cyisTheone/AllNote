"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
示例 3：

输入：nums = [1,0,1,2]
输出：3
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest = 0
        for num in num_set:
            # 当前数字减去1不在数组里，说明他是一组数的开头，可以计算
            if num - 1 not in num_set:
                current_num = num
                # 初始长度置为1
                current_length = 1
                # 从当前数字开始每次+1，判断是否在数组里，在的话长度计数+1
                while current_num + 1 in num_set:
                    current_length += 1
                    current_num += 1
                # 更新最大长度
                longest = max(longest, current_length)
        return longest


if __name__ == "__main__":
    solution = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    result = solution.longestConsecutive(nums)
    print(result)  # Output: 4
