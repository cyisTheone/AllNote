"""
二分查找搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。



示例 1:

输入: nums = [1,3,5,6], target = 5
输出: 2
示例 2:

输入: nums = [1,3,5,6], target = 2
输出: 1
示例 3:

输入: nums = [1,3,5,6], target = 7
输出: 4

"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)

        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 中间数小于目标值，说明目标在mid右边， 缩小左边边界，更新l为mid+1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return l


if __name__ == "__main__":
    S = Solution()
    res = S.searchInsert([1, 3, 5, 6], 5)
    print(res)  # output 2
