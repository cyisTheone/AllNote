"""
leetcode22 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。



示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]

"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        # path存放括号，长度是2n
        path = [""] * 2 * n

        def dfs(l, r):
            if r == n:  # 右括号个数等于n，找到答案
                ans.append("".join(path))
                return

            #  要么先放左括号，要么先放右括号
            if l < n:  # 左括号个数小于n，继续放入左括号
                path[l + r] = "("  # 填左括号
                dfs(l + 1, r)
            if l > r:  # 左括号个数大于右括号，放入右括号
                path[l + r] = ")"  # 填右括号
                dfs(l, r + 1)

        dfs(0, 0)
        return ans


if __name__ == "__main__":
    S = Solution()
    res = S.generateParenthesis(3)
    print(res)  # output ['((()))', '(()())', '(())()', '()(())', '()()()']
