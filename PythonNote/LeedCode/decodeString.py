"""
leetcode 394
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

测试用例保证输出的长度不会超过 105。



示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：

输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"

"""


class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        cur_str = ""
        cur_num = 0

        for c in s:
            if c == "[":
                # 遇到[，将[前面的字符串和，[里面未来需要重复的次数入栈， 弹出时再将[前面的字符串和[后面的串乘以num后想加
                stack.append((cur_str, cur_num))
                cur_str = ""
                cur_num = 0
            elif c.isdigit():
                # 遇到数字，累加到curr_num里， 10进制需要当前cur_num *10 ，例如12， 第一次读取到1，cur_num=1，第二次读取到2， cur_num=1*10+2=12
                cur_num = cur_num * 10 + int(c)
            elif c == "]":
                pre_str, cyc_num = stack.pop()
                cur_str = pre_str + cyc_num * cur_str
            else:
                # 普通字符串直接追加到当前字符串后面
                cur_str += c

        return cur_str


if __name__ == "__main__":
    S = Solution()
    res = S.decodeString("3[a2[c]]")
    print(res)  # output "accaccacc"
