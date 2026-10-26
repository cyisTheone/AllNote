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
        
        n = len(nums)
        max_sum = 0
        if n==1:
            max_sum = nums[0]
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if s <= 0 and max_sum == 0:
                    max_sum = min(max_sum, s)
                max_sum = max(max_sum, s)
        return max_sum

    def maxSubArray1(self, nums: List[int]) -> int:
        """
        动态规划版本
        """
        n = len(nums)
        max_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, n):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum

if __name__ == "__main__":
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = solution.maxSubArray1(nums)
    print(result)  # Output: 6