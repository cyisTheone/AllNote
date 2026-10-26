"""
用户输入一个二维数组，旋转角度，角度是 90 的整倍数，返回旋转后的二维数组
"""


def rotate(matrix, angle):
    # 兼容负角度， -90%360=270
    times = (angle % 360) // 90

    # 单次旋转90度函数
    def transpose(matrix):
        # 行
        m = len(matrix)
        # 列
        n = len(matrix[0])
        # 转置后， n行m列，初始化
        new_mat = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                new_mat[j][i] = matrix[i][j]
        # 对每一行列表反转
        for col in new_mat:
            col.reverse()
        return new_mat

    # 需要旋转90度的次数
    for _ in range(times):
        matrix = transpose(matrix)
    return matrix

matrix = [
    [1, 2, 3, 30],
    [4, 5, 6, 60],
    [7, 8, 9, 90]
]


print(rotate(matrix, 270))
