"""
leetcode 41
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
 

示例 1：

输入：nums = [1,2,0]
输出：3
解释：范围 [1,2] 中的数字都在数组中。
示例 2：

输入：nums = [3,4,-1,1]
输出：2
解释：1 在数组中，但 2 没有。
示例 3：

输入：nums = [7,8,9,11,12]
输出：1
解释：最小的正数 1 没有出现。
"""
import collections
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 哈希表记录每个数出现的次数
        dp = collections.defaultdict(int)
        for num in nums:
            dp[num] +=1

        ans = 1

        if max(nums) <=0:
            return 1

        # 从1开始检查，直到找到缺失的正整数
        for i in range(1, max(nums)+2):
            if i not in dp:
                ans = i
                break

        return ans

if __name__ == "__main__":
    solution = Solution()
    nums =[3,4,-1,1]
    result = solution.firstMissingPositive(nums)
    print(result)  # Output: 2