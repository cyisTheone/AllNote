class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def helper(nums, target):
            n = len(nums)
            l = 0
            r = n - 1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        start = helper(nums, target)
        # 如果找到的start下标等于数组长度，或者start所在的数不等于target，说明不在数组内
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = helper(nums, target + 1) - 1
        return [start, end]

if __name__ == "__main__":
    S = Solution()
    res = S.searchRange([5,7,7,8,8,10], 6)
    print(res) # output [-1, -1]
    res1 = S.searchRange([5,7,7,8,8,10], 8)
    print(res1) # output [3,4]