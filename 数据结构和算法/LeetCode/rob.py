"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

"""

from ast import List


class Solution:

    """
    状态转移方程
    dp[i] = max(dp[i-2] + nums[i], dp[i-1])

    第N个房间的偷窃金额等于第N-2个房间的偷窃金额加上第N个房间的金额，或者第N-1个房间的偷窃金额，取两者的最大值。
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==0:
            return 0
            
        dp = [0] * n

        for i in range(0, n):
            if i == 0:
                dp[0] = nums[0]
            elif i == 1:
                dp[1] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return max(dp)

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 9, 3, 1]
    result = solution.rob(nums)
    print(result)  # Output: 12