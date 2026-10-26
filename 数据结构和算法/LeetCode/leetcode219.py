"""
https://leetcode.cn/problems/contains-duplicate-ii/description/
给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。



示例 1：

输入：nums = [1,2,3,1], k = 3
输出：true
示例 2：

输入：nums = [1,0,1,1], k = 1
输出：true
示例 3：

输入：nums = [1,2,3,1,2,3], k = 2
输出：false
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        st = set()

        for idx, num in enumerate(nums):
            # 先判断set里是否有当前遍历的元素，有就返回True
            if num in st:
                return True
            # 否则加入到set
            st.add(num)
            # 判断set长度是否大于k了，大于需要将前面的元素移除，也就是nums[idx-k]
            if len(st) > k:
                st.remove(nums[idx - k])
        # 遍历结束，返回False
        return False


if __name__ == "__main__":

    nums1 = [1, 2, 3, 1]
    k1 = 3
    nums2 = [1, 0, 1, 1]
    k2 = 1
    nums3 = [1, 2, 3, 1, 2, 3]
    k3 = 2

    S = Solution()
    for num, k in zip([nums1, nums2, nums3], [k1, k2, k3]):
        print(S.containsNearbyDuplicate(num, k))  # ouput True True False
