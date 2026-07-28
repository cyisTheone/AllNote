
"""
LeetCode Problem 283: Move Zeroes
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

 

示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]
"""

from ast import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        zero_point = 0
        for i in range(n):
            if nums[i]:
                nums[zero_point] = nums[i]
                zero_point +=1
        
        for i in range(zero_point, n):
            nums[i] = 0


    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        双指针初始位置均为0，左指针记录非0的末尾，右指针记录向右移动，遇到非0的就和左指针交换位置
        """
        n = len(nums)
        left = right = 0

        while(right < n):
            # 如果右指针指向的元素不为0，则交换左指针和右指针的元素，并将左指针向右移动一位
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1
            right +=1
            

if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(nums)  # Output: [1, 3, 12, 0, 0]
    solution.moveZeroes1(nums)
    print(nums)  # Output: [1, 3, 12, 0, 0]