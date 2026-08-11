from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)

        def dfs(path, start_index):

            if sum(path) > target:
                return

            if sum(path) == target:
                ans.append(path)
                return

            for i in range(start_index, n):
                path.append(candidates[i])
                dfs(path, i)
                path.pop()

        dfs([], 0)
        return ans


if __name__ == "__main__":
    S = Solution()
    res = S.combinationSum([2, 3, 6, 7], 7)
    print(res)  # output
