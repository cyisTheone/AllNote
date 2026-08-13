from typing import List
import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        n = len(s)
        lp = len(p)

        sortp = "".join(sorted(p))
        ans = []
        for i in range(n - lp + 1):

            ip = "".join(sorted(s[i:i + lp]))
            if ip == sortp:
                ans.append(i)
        return ans

    def findAnagrams1(self, s: str, p: str) -> List[int]:

        n = len(s)
        lp = len(p)

        # 定义两个哈希表，记录每个字母出现的次数， p_counter固定，用来比较
        p_counter = collections.Counter(p)
        # wind_counter固定长度为p的长度，初始位置为字符串p的长度
        window_couter = collections.Counter(s[:lp - 1])

        # 右边界从p长度开始
        r = lp - 1
        l = 0
        ans = []
        while r < n:
            # 将当前字母加入window中
            window_couter[s[r]] += 1
            # 比较两个窗口是否相等，相等ans中加入widow的起始位置
            if p_counter == window_couter:
                ans.append(l)
            r += 1
            # 窗口左边界右移动（即将索引对应的计数-1）
            window_couter[s[l]] -= 1
            # 计数为0，则删除该元素
            if window_couter[s[l]] == 0:
                del window_couter[s[l]]
            l += 1
        return ans


if __name__ == "__main__":
    S = Solution()
    res = S.findAnagrams("abab", "ab")
    print(res)  # ouput 0,1,2
    res1 = S.findAnagrams1("cbaebabacd", "abc")
    print(res1)  # ouput 0,6
