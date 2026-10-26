"""
小明设计了一条灯带，该灯带中共有 16 盏灯（编号 0 到 15），每盏灯有两种颜色：红色（用字符 R 表示）和绿色（用字符 G 表示）。每过一秒，灯带中的灯都会按照以下规则进行一次颜色变换：

如果上一秒灯 lights[i] 的两个相邻灯 lights[i-1] 和 lights[i+1] 颜色一致，则灯 lights[i] 在当前秒需要设置为绿色。
其他场景（相邻灯颜色不一致、或灯只有单一邻居），则该灯在当前秒需要设置为红色。
注意：灯带中编号为 0 的灯和编号为 15 的灯是不相邻的（线性灯带，首尾不相连）。因此编号 0 的灯只有右邻居，编号 15 的灯只有左邻居。

给定一个灯带的初始状态，请你输出 t 秒后灯带中各灯的颜色。


时间够大，灯带颜色必然会出现循环， 实质是求一个起点开始的环的起始位置和大小
"""


def step_calc(light):
    "计算某条灯带下一秒的结果"

    count = 0
    s = ["R"] * 16
    # s[0] = s[-1] = "R"
    for i in range(1, 15):
        if light[i - 1] != light[i + 1]:
            s[i] = "R"
        else:
            s[i] = "G"
    return "".join(s)


def light_color(lights, times):
    # 定义哈希表，记录历史状态, 每秒一个状态
    history_status = [] # 注意初始状态不要入环，走到某一个状态后后续的才有可能入环

    new_stat = lights
    for t in range(times):
        # 计算下一秒灯带的颜色
        new_stat = step_calc(new_stat)
        # 下一秒的颜色在历史记录中，说明走到了环的起点
        if new_stat in history_status:
            # 此时的stat就是环的起点
            loop_start = history_status.index(new_stat)
            # 环长是history_status的长度
            loop_len = len(history_status) - loop_start
            # 剩余没有计算的时间，都是在循环这个环
            remain = times - t
            # 剩余时间除以环长，剩余的步数加上起点就是对应的灯带颜色
            return history_status[loop_start + (remain % loop_len)]
        history_status.append(new_stat)

    # 循环走完还没入环，直接返回
    return new_stat


if __name__ == "__main__":
    lights = "RRRRRRRRRRRRRRRR"
    print(light_color(lights, 1))  # output RGGGGGGGGGGGGGGR
    print(light_color(lights, 30))  # output RRRRRRRRRRRRRRRR,  这种起始30次会走完一个循环
