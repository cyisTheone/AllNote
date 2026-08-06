"""
有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。


示例 1：

输入：s = "()"

输出：true

示例 2：

输入：s = "()[]{}"

输出：true

示例 3：

输入：s = "(]"

输出：false

示例 4：

输入：s = "([])"

输出：true

示例 5：

输入：s = "([)]"

输出：false
"""


class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2:
            return False

        mp = {"{": "}", "[": "]", "(": ")"}
        stack = []
        for c in s:
            # 如果字符在mp里，说明是左括号{[(
            if c in mp:
                # 将value入栈，即每个左括号对应的右括号，未来弹出时，需要有后序的c与之匹配
                stack.append(mp[c])
            # 如果弹出的值和key不相等，说明括号不成对， 栈为空，也说明不成对
            elif not stack or stack.pop() != c:
                return False
        # 栈为空全部成对处理，返回True
        return not stack


if __name__ == "__main__":
    S = Solution()
    res = S.isValid("({}[]())")
    print(res)  # output True

    res1 = S.isValid("({}[]))")
    print(res1)  # output False
