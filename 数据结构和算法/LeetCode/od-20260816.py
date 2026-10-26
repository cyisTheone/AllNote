"""
题目描述
电池充电过程并非恒定电流，而是遵循一定的充电曲线。给定电池容量、当前电量百分比、目标电量百分比和充电器最大输出电流，请计算充电至目标电量所需的时间。
充电曲线规则如下：
当电量 < 20% 时，采用预充模式，电流为最大电流的 20%；
当电量 ≥ 20% 且 < 80% 时，采用恒流模式，电流为最大电流的 100%；
当电量 ≥ 80% 时，采用恒压模式，电流随电量增加而线性衰减。
电流计算公式：
current(soc) = maxCurrent × (1 − (soc − 80) × 0.045)
其中 soc 为电量百分比，该公式保证 current(80)=maxCurrent，current(100)=maxCurrent × 0.1。
每充入 batteryCapacity × 1% 的电量，根据当前电量所在阶段确定该步进的充电电流，然后累加该步进所需的时间。
由于恒压阶段电流线性衰减，可使用平均电流法计算充电时间：
平均电流 = (起始电流 + 结束电流) / 2
输入描述
本题为核心代码模式，你需要实现函数 chargingTime(batteryCapacity, maxCurrent, initialSOC, targetSOC)。
参数：
batteryCapacity：电池容量，单位 mAh，整型，范围 1000 ~ 10000。
maxCurrent：充电器最大输出电流，单位 mA，整型，范围 500 ~ 10000。
initialSOC：为当前电量百分比，整型，范围 0 ~ 100。
targetSOC：为目标电量百分比，整型，范围 initialSOC ~ 100。
输出描述
返回充电至目标电量所需的时间，浮点数，保留一位小数（四舍五入）。
样例 1
输入：
batteryCapacity = 3000, maxCurrent = 1500, initialSOC = 0, targetSOC = 100
输出：
3.9

"""
from decimal import Decimal, ROUND_HALF_UP


def round_self(n, digths):
    template = Decimal("0." + "0" * digths)
    return float(Decimal(str(n)).quantize(template, rounding=ROUND_HALF_UP))


def main(battery, maxcurrent, initsoc, targetsoc):
    # 每1%需要的电量
    delta_cap = battery * 0.01

    # 初始化答案为0.0
    ans = 0.0

    # 初始化电量
    soc = initsoc

    while soc < targetsoc:
        if soc < 20:
            t = delta_cap / (maxcurrent * 0.2)
            ans += t
            soc += 1
        if 20 <= soc < 80:
            t = delta_cap / maxcurrent
            ans += t
            soc += 1
        if soc >= 80:
            start = maxcurrent
            end = maxcurrent * (1 - (targetsoc - 80) * 0.045)
            avg = (start + end) / 2
            t = (delta_cap * (targetsoc - 80)) / avg
            ans += t
            soc = targetsoc
    return round_self(ans, 1)


if __name__ == "__main__":
    battery = 3000
    maxcurrent = 1500
    initsoc = 0
    targetsoc = 100

    print(main(battery, maxcurrent, initsoc, targetsoc))
