import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 计算每一个元素的前缀和加入到set中， 然后减去目标值k后 如果在set中，则存计数+1
        # key是前缀和，值是前缀和出现的次数
        mp = collections.defaultdict(int)
        mp[0] = 1  # 哨兵,避免漏掉前缀和为k的情况

        pre_sum = 0
        count = 0
        for num in nums:
            pre_sum += num
            # 先查询，再存入
            if pre_sum - k in mp:
                # 前缀和出现的次数更新到计数中
                count += mp[pre_sum - k]
            mp[pre_sum] += 1
        return count


if __name__ == "__main__":
    S = Solution()
    res = S.subarraySum([1, 2, 3], 3)
    print(res)  # ouput 2
