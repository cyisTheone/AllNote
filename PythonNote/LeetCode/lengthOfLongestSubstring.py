"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        n = len(s)
        l = r = 0
        occ = set()
        while r < n:
            ans = max(ans, len(occ))
            # 判断右指针指向的当前数是否在set里,不在则加入
            if s[r] not in occ:
                occ.add(s[r])
                r += 1
            # elif里的 这一步很关键，为什么是判断左指针的元素是否在set里，并删除？
            # while循环用右指针遍历，将元素加入set，遇到加不进去的元素，就要把这个元素之前的所有元素从set里删除，左指针需要不停的循环删除并且右移，直到右指针的元素可以成功加入
            # 所以当右指针元素已经在set里时，就要判断左指并删除set的元素知道右指针元素可以加入
            elif s[l] in occ:
                occ.remove(s[l])
                l += 1

        return ans

if __name__ == "__main__":
    S = Solution()
    res = S.lengthOfLongestSubstring("pwwkew")
    print(res) # ouopt 3