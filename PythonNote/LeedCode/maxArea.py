"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1

"""


class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)

        # 双指针法，左右指针分别指向数组的两端，计算当前面积，并更新最大面积。然后移动较短的指针，直到两个指针相遇。
        left = 0
        right = n - 1
        total = 0
        while left < right:
            ans = min(height[left], height[right]) * (right - left)
            total = max(total, ans)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return total


if __name__ == "__main__":
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = solution.maxArea(height)
    print(result)  # Output: 49
