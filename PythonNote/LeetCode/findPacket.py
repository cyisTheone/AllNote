"""
题目描述
在数据包传输系统中，为了优化网络带宽利用率，系统需要对数据包序列进行处理，找出每个数据包右侧第一个满足某些条件、优先级更高的数据包。

每个数据包的格式为：<priority>:<weight>，其中：

<priority> 是数据包的优先级（正整数，1 ≤ priority ≤ 10^5，数值越大优先级越高）
<weight> 是数据包的权重（正整数，1 ≤ weight ≤ 10^5）
系统需要按照以下规则处理数据包：搜索整个数据包序列（从左到右），对于每个数据包，找出其右侧第一个同时满足如下条件的数据包：

条件1：目标数据包的 priority 必须大于当前数据包的 priority
条件2：目标数据包的 weight 必须等于当前数据包的 weight
请编写一个方法，实现数据包右侧第一个满足条件的数据包查找功能。

输入描述
参数 packets：数据包内容，长度为 n（正整数，1 ≤ n ≤ 10^5）的数组，每个元素为 [priority, weight]。

输出描述
右侧第一个满足条件的数据包 ID 组成的数组序列；数据包 ID 是其在数组中的位置，即第 i 个数据包的 ID 为（从 1 开始计数，非数组下标 0）；如果某个数据包右侧没有满足条件的数据包，则输出 0。

示例1
输入

[[5,10],[6,10],[4,10]]
输出

[2,0,0]
说明

数据包序列：[[5,10],[6,10],[4,10]]

第 1 个数据包 [5,10] 右侧搜索：

第 2 个 [6,10]：priority(6) > 5，weight(10) 相同，满足条件，输出 2（非数组下标 1）

"""

from collections import defaultdict


def main(packets):
    # p:w , p>p ,w=w
    # 用哈希表存储每个权重相同的数据包， key是w， v是packet
    n = len(packets)
    hashtable = defaultdict(list)
    ans = [0] * n

    for i in range(n - 1, -1, -1):
        p, w = packets[i]
        # 取出权重为当前w的单调栈，这里w没有的话，会自动创建
        stack = hashtable[w]

        # 遍历当前栈，寻找比p大的元素
        while stack and stack[-1][0] < p:
            stack.pop()  # 弹出比p小的栈顶元素

        # 判断此时栈是否为空，为空则没有答案，不为空，栈顶元素就是答案, 注意这里的栈存入的元素是p和当前的索引 (P, i+1), i+1 是为了直接取出答案，答案要求的是从1开始
        if stack:
            ans[i] = stack[-1][1]
        else:
            ans[i] = 0

        stack.append((p, i + 1))  # 存入packcet的下标+1

    return ans

if __name__ == "__main__":
    packets1 = [[5, 10], [6, 10], [4, 10]]
    print("最终输出：", main(packets1)) # output [2, 0, 0]
