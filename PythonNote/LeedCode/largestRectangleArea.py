"""
leetcode 84
柱状图中的最大矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 暴力解法
        n = len(heights)
        ans = 0

        for i in range(n):

            h = heights[i]

            l = r = i
            # 向左循环计算，找到比第一个比i小的那个元素的索引
            while l > 0 and heights[l - 1] >= h:
                l -= 1
            # 向右循环计算，找到第一个比i小的那个元素的索引
            while r < n - 1 and heights[r + 1] >= h:
                r += 1

            area = h * (r - l + 1)
            ans = max(ans, area)

        return ans

    def largestRectangleAreaOsStack(self, heights: List[int]) -> int:

        heights.append(0)  # 哨兵0，强行将0入栈，0比所有的元素都小，会让所有元素出栈
        n = len(heights)
        stack = []

        ans = 0

        for i in range(n):

            # while循环处理，要入栈的元素比栈顶小，栈顶弹出，要入栈的元素可能还是比新的栈顶元素小，继续弹出，并计算面积
            while stack and heights[i] < heights[stack[-1]]:
                curr = stack.pop()
                r = i  # 有边界就是此时的i
                l = stack[-1] if stack else -1  # 左边界就是新的栈顶
                area = heights[curr] * (
                        r - l - 1
                )  # 宽度是r-l-1，因为左右是宽度的边界，但不含该边界（左右都比当前高度小，不可包含）
                ans = max(ans, area)

            stack.append(i)

        return ans


if __name__ == "__main__":
    S = Solution()
    res = S.largestRectangleArea([2, 1, 5, 6, 2, 3])
    print(res)  # output 10
    res1 = S.largestRectangleAreaOsStack([2, 1, 5, 6, 2, 3])
    print(res1)  # output 10
