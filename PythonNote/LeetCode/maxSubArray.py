# 动态规划题解，https://leetcode.cn/problems/maximum-subarray/solutions/9058/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/?envType=study-plan-v2&envId=top-100-liked
"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。



示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23

"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            # dp[i-1]存在小于0的情况，所以小于0时，选当前值作为dp[i], 即nuns[i]之前的数加起来小于等于0，继续累加没有意义
            dp[i] = max(nums[i], nums[i] + dp[i - 1])

        return max(dp)


if __name__ == "__main__":
    S = Solution()
    res = S.maxSubArray([-2, 1])
    print(res)  # output 1
