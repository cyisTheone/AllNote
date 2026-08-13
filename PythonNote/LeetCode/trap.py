"""
leetcode接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        # 定义两个指针，左右开始遍历
        l = 0
        r = n - 1
        # 定义结果
        s = 0
        # 定义左右的最大值
        max_l = height[l]
        max_r = height[r]

        while l < r:
            # 哪边小就移动哪边，每个点接到的雨水取决于他的左右两边的最小值
            if max_l <= max_r:
                l += 1
                # 左边的最大值比自己还小，取自身为最大值来计算
                max_l = max(max_l, height[l])
                s += (max_l - height[l])
            else:
                r -= 1
                # 右边的最大值比自己还小，取自身为最大值来计算
                max_r = max(max_r, height[r])
                s += (max_r - height[r])
        return s


if __name__ == "__main__":
    S = Solution()
    res = S.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(res)  # ouput 6
