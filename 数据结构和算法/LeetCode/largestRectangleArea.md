# LeetCode 84 柱状图中最大的矩形

> 题目：给定 n 个非负整数，表示柱状图各个柱子的高度，求柱状图中能够勾勒出的最大矩形面积。
> 
> 示例输入：`heights = [2,1,5,6,2,3]`
> 
> 输出：`10`
> 
> 

## 暴力解法（O\(n²\)，仅用于理解，会超时）

> 思路：以每根柱子作为矩形高度，向左右双向扩散，直到遇到比自身高度更小的柱子，计算矩形面积。
> 
> 特点：left、right 是矩形可以包含的端点，闭区间；宽度公式 `width = right - left + 1`
> 
> 

```python
def largestRectangleArea_brute(heights):
    n = len(heights)
    max_area = 0
    for i in range(n):
        h = heights[i]
        # 向左扩散
        left = i
        while left > 0 and heights[left - 1] >= h:
            left -= 1
        # 向右扩散
        right = i
        while right < n - 1 and heights[right + 1] >= h:
            right += 1
        # 计算面积
        width = right - left + 1
        area = h * width
        max_area = max(max_area, area)
    return max_area


if __name__ == "__main__":
    print(largestRectangleArea_brute([2, 1, 5, 6, 2, 3]))  # 10
    print(largestRectangleArea_brute([2, 4]))              # 4
```

## 单调递增栈解法（AC，O\(n\)）

> 思路：单调递增栈保存柱子下标，找到每根柱子**左右第一个高度更小的边界**。
> 
> - left：左边第一个比当前高度小的下标
> 
> - right：右边第一个比当前高度小的下标
> 
> - left、right 为不可包含的开区间边界，宽度公式：`width = right - left - 1`
> 
> - 末尾追加哨兵 0，自动清算栈内剩余元素，无需额外收尾逻辑
> 
> 

```python
def largestRectangleArea_stack(heights):
    stack = []
    max_area = 0
    # 哨兵0，强制把栈中所有元素弹出计算
    heights.append(0)

    for i in range(len(heights)):
        # while：持续弹出所有满足条件的栈顶，不能使用if，if只会弹出一次
        while stack and heights[i] < heights[stack[-1]]:
            h_idx = stack.pop()
            h = heights[h_idx]
            # 栈空代表左侧没有更小柱子，边界赋值为 -1
            if not stack:
                left = -1
            else:
                left = stack[-1]
            right = i
            width = right - left - 1
            area = h * width
            max_area = max(max_area, area)
        stack.append(i)
    return max_area


if __name__ == "__main__":
    print(largestRectangleArea_stack([2, 1, 5, 6, 2, 3]))  # 10
    print(largestRectangleArea_stack([2, 4]))              # 4
```

## 暴力与单调栈核心对比

|项目|暴力解法|单调递增栈解法|
|---|---|---|
|时间复杂度|O\(n²\)|O\(n\)|
|边界含义|left、right 为矩形可包含端点（闭区间）|left、right 为屏障边界（开区间，不纳入矩形）|
|宽度公式|right‑left\+1|right‑left‑1|
|缺点|重复扫描，大数据用例超时|逻辑抽象，需要理解栈的弹出时机|
|循环弹出|嵌套 while 双向扫描|for \+ 内部 while，一次性找全部边界|

## 关键易错点

1. **必须用 while，不能用 if**：同一个 i 可能会触发栈内多个元素连续弹出，if 只会处理一个元素，结果错误。

2. 栈内存**下标**，不是高度，依靠下标取原数组值、计算宽度。

3. 栈空时左边界设置为 `-1`，不能设置为 0。

4. 哨兵 `heights.append(0)`，处理数组末尾残留的递增柱子。

5. **宽度公式误区**：单调栈中 left、right 是屏障边界（开区间），不能纳入矩形，因此宽度公式为 `right - left - 1`，而非 `right - left + 1`（暴力解法闭区间公式）。

## 宽度公式（r\-l\-1）核心解析

### 核心逻辑

单调栈中，left 和 right 是**左右第一个比当前柱子高度小的屏障下标**，属于开区间边界（不包含在矩形内），矩形实际可用区间为 `(left, right)`，因此宽度需用 `right - left - 1` 计算（排除左右两个屏障）。

### 示例验证（heights = \[2,1,5,6,2,3\]，柱子 h=5，下标 i=2）

- left=1（值=1，左边第一个比5小的屏障）

- right=4（值=2，右边第一个比5小的屏障）

- 可用柱子：下标2、3（共2根）

- 公式计算：`4 - 1 - 1 = 2`，与实际宽度一致。

### 边界案例（left=\-1）

当柱子左侧无更小元素时，left 赋值为 \-1（虚拟屏障），例如 heights=\[2\]，补哨兵0后：

- left=\-1，right=1（哨兵下标）

- 公式计算：`1 - (-1) - 1 = 1`，宽度正确。

### 与暴力解法对比

- 暴力解法：left、right 是矩形可包含的端点（闭区间），公式为 `right - left + 1`。

- 单调栈解法：left、right 是屏障（开区间），公式为 `right - left - 1`，核心区别在于边界是否纳入矩形。

## 模拟示例：`[2,1,5,6,2,3]`

补哨兵后数组变为 `[2,1,5,6,2,3,0]`

- i=4，height=2，连续弹出下标3\(h=6\)、下标2\(h=5\)

- i=6，height=0，哨兵触发，把栈中剩余全部元素弹出完成计算

## 同类单调栈对照题

|题号|题目|栈类型|弹出条件|
|---|---|---|---|
|739|每日温度|单调递减栈|当前值 \> 栈顶值，找下一个更大|
|84|柱状图中最大矩形|单调递增栈|当前值 \< 栈顶值，找下一个更小|

> （注：部分内容可能由 AI 生成）
