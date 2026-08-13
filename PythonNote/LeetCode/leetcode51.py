from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = []
        path = [["."] * n] * n

        def checkVaild():
            pass

        def dfs(row):
            if row == n:
                res = path.copy()
                print(res)
                ans.append(res)
                return

            for col in range(n):
                path[col][row] = 'Q'
                # print(path)
                dfs(row+1)
                path[col][row] = '.'
        dfs(0)
        return  ans

if __name__ == "__main__":
    S = Solution()
    res = S.solveNQueens(4)
    print(res)  # output [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]