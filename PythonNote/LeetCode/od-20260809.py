"""
题目描述
云南的菌子加工厂要加工一批野生菌，所有菌子同时进厂。由于菌子新鲜度随时间流失，价值不断衰减。工厂不能同时加工菌子，即逐个串行加工，正在加工的菌子价值不再衰减，加工完毕立即售卖。
已知每个菌子的初始市场价值和新鲜度衰减速度（每小时损失的价值），菌子的实际价值 = 初始价值 - 衰减速度 × 从进入工厂到开始加工的等待时间。在给定时间内，合理安排加工顺序使得加工完成的菌子总价值最大化。
每个菌子的加工时间固定为 5 小时，加工所有菌子的总耗时不能超过给定的总加工时间。若菌子的实际价值衰减至零或负值，则不能再售卖，即不需要参与加工。
输入描述
输入为四行：
count
total
values
decays
count 表示菌子数量，1 <= count <= 15
total 表示可用总加工时间，5 <= total <= 75，单位小时
values [i] 表示第 i 个菌子的初始市场价值
decays [i] 表示第 i 个菌子的衰减速度
数组 values 和 decays 按示例使用英文逗号分隔。
输出描述
输出一个整数，表示在给定时间内能加工完成的菌子的最大总价值。

"""


def main(count, total, values, decays):
    limit = total / 5

    full = 1 << count # 表示2的count次方
    dp = [-1] * full

    # 初始化全0收益为0
    dp[0] = 0
    best = 0

    for mask in range(full):
        # 下面的循环会更新dp中某个mask的状态，需要判断
        if dp[mask] < 0:
            continue

        # 计算已经加工的菌子个数，统计二进制中“1”的个数
        done = bin(mask).count("1")
        best = max(best, dp[mask])

        if done >= limit:
            continue
        # 等待时间
        wait = done * 5

        # 用当前状态去循环每一个菌子，尝试加进来加工，
        for i in range(count):
            # 右移i位和 1 做按位与, 都为1，说明i这个菌子加工过，需要跳过，  011 >> 1 = 01, 01&1 = 1, 代表第二个菌子加工过， 011>>2=0, 0&1=0,  代表第三个菌子加没有工过
            if mask >> i & 1:
                continue
            # 当前菌子的剩余价值，如果剩余价值小于0，跳过加工
            gain = values[i] - decays[i] * wait
            if gain <= 0:
                continue

            # 都符合条件，开始加工，计算新的价值， 构造新状态, 在mask的基础上将第i位置为1
            new_mask = mask | (1 << i)
            """
            代码解读
            假设 mask = 0b011（十进制 3），代表已经选了 0 号、1 号菌子。
            现在 i=2，1<<2 = 0b100
            mask      = 0 1 1
            1 << i    = 1 0 0
            ---------------- |或
            new_mask  = 1 1 1
            new_mask=0b111，代表现在选了 0,1,2 三个菌子。
            """
            # 更新状态收益
            dp[new_mask] = max(dp[new_mask], dp[mask] + gain)

    return best


if __name__ == "__main__":
    count = 3
    total = 15
    values = [20, 10, 15]
    decays = [3, 1, 2]
    print(main(count, total, values, decays))  # output 15
