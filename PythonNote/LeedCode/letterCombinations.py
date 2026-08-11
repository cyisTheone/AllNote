"""
leetcode 17， 回溯， 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。





示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = "2"
输出：["a","b","c"]

"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        ans = []
        s = []
        # 将输入的字符串转为列表， “23” -> [2,3]，后续用索引0,1来取2 3
        num_digits = [int(i) for i in digits]

        # 入参index表示的是顺序处理， 从0开始，
        def backtrack(index):
            # 定义终止条件
            if index == len(num_digits):  # 等价于 len(s) == len(num_digits),
                ans.append("".join(s))
                return
            # 本次要遍历的字符串
            strs = mp[num_digits[index]]

            for i in range(len(strs)):
                s.append(strs[i])
                backtrack(index + 1)
                s.pop()

        backtrack(0)

        return ans


if __name__ == "__main__":
    S = Solution()
    res = S.letterCombinations("23")
    print(res)  # output ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
