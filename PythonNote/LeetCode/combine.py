"""
leetcode 77
回溯算法，组合
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。



示例 1：

输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
示例 2：

输入：n = 1, k = 1
输出：[[1]]

"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        path = []

        def backtraking(start_index):

            if len(path) == k:
                ans.append(path.copy())
                return

            for i in range(start_index, n + 1):
                path.append(i)
                backtraking(i + 1)
                path.pop()

        backtraking(1)

        return ans


if __name__ == "__main__":
    S = Solution()
    res = S.combine(4, 2)
    print(res)  # output [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
