"""
leetcode131 分割回文串
给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。



示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans = []
        path = []
        n = len(s)

        def dfs(start_index):
            if start_index == n:
                ans.append(path.copy())
                return

            for i in range(start_index, n):
                # 以start_index起始的， 结尾的就是本轮分割的子串
                subs = s[start_index:i + 1]
                if subs == subs[::-1]:
                    path.append(subs)
                else:
                    continue
                dfs(i + 1)
                path.pop()

        dfs(0)
        return ans


if __name__ == "__main__":
    S = Solution()
    res = S.partition("aab")
    print(res)  # output [["a","a","b"],["aa","b"]]
