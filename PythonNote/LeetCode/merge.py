"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

 

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
示例 3：

输入：intervals = [[4,7],[1,4]]
输出：[[1,7]]
解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。

贪心算法
 
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 按每个数组的做边界排序
        intervals.sort(key=lambda x: x[0])

        # 定义一个空数组保存答案
        ans = []
        
        for each in intervals:
            # 遍历每个数组，判断数组的左边界是否比已合并的数组的最后一个的右边界大，大说明不相交，直接追加这个数组
            if not ans or each[0] > ans[-1][1]:
                ans.append(each)
            
            # 否则的话，需要更新已合并数组的右边界，取当前元素和ans数组最后一个元素右边界的最大值
            else:
                ans[-1][1] = max(each[1], ans[-1][1])
        return ans

    if __name__ == "__main__":
        solution = Solution()
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        result = solution.merge(intervals)
        print(result)  # Output: [[1,6],[8,10],[15,18]]