"""
基站运维团队需要统计某区域基站的低能耗连续运行时段数目，以评估基站的节能优化效果，给定以下信息：
整数数组power， power[i]表示该基站第i小时的能耗值（单位：千瓦时），能耗不会为负。
整数target，表示低能耗阈值（单位；千瓦时），要求连续时段的总能耗不超过该阈值。
整数maxHour，表示最大统计时长（单位：小时），要求连续时段的时长不超过该值，且至少为1小时。
请统计满足以下两个条件的连续运行时段（子数组）的数目
1、连续时段的时长落在[1，maxHour]内；
2、该时段内的总能耗不超过target

实现函数countLowPowerPeriods(power, target, maxHour)

样例1
输入
power=[0,0,0], target=0, maxHour=2
输出
5
"""


def countLowPowerPeriods(power, target, maxhour):
    """
    暴力解法
    """
    n = len(power)

    ans = 0

    for i in range(n):
        s = 0
        # 子数组下标j的范围是i到i+maxHour或者最大到n，原数组长度
        for j in range(i, min(n, i + maxHour)):
            s += power[j]
            if s <= target:
                ans += 1
            else:
                break
    return ans


def countLowPowerPeriods1(power, target, maxhour):
    """
    双指针解法，l和r初始都为0，右指针遍历元素，计算l到r之间的和
    对于满足和的子数组[l,r],还要找出合法长度，即小于maxHour
    由于power数组为非复数，[l+1, r]的和始终小于等于[l,r]，找到min_l之后，r-min_l+1就是以该r为右端点的所有数量
    """
    left = 0
    total = 0
    res = 0
    for right in range(len(power)):
        total += power[right]
        # 总和超过阈值，收缩左边界，然后计算以该右边界结尾的子数组
        while total > target:
            total -= power[left]
            left += 1
        # 起点不能早于 left，也不能早于 right-maxhour+1（限制最大长度）
        start_min = max(left, right - maxhour + 1)
        #  由于power数组为非复数，[l+1, r]的和始终小于等于[l,r]， 找到min_l之后，r-min_l+1就是以该r为右端点的所有数量
        # 区间内总和具有单调性，如果有负数，这题解法不适用
        cnt = right - start_min + 1
        res += cnt
    return res


power = [0, 0, 0, 0, 0]
target = 0
maxHour = 3

res = countLowPowerPeriods(power, target, maxHour)
print(res)
