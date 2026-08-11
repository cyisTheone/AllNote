"""
leetcode 46
回溯算法，全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。



示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]

"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        n = len(nums)
        used = [False] * n

        def backtrack(path=[]):
            # 定义终止条件
            if len(path) == n:
                ans.append(path.copy())
                return

            for i in range(n):
                # 如果当前元素标记被使用，则不参与循环
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack()
        return ans


if __name__ == "__main__":
    S = Solution()
    res = S.permute([1, 2, 3])
    print(res)  # output [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
