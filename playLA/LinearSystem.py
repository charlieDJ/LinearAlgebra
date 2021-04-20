from .Matrix import Matrix
from .Vector import Vector


class LinearSystem:
    def __init__(self, A, b):
        assert A.row_num() == len(b), \
            "Matrix A's row num must equals b's length!"
        self._m = A.row_num()
        self._n = A.col_num()
        assert self._m == self._n  # todo no this restriction

        """让A矩阵的第i行的末尾添加B向量第i个元素"""
        self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]])
                   for i in range(self._m)]

    # 查找index行index列最大的值
    def _max_row(self, index, n):
        """ret:最优行数"""
        best, ret = self.Ab[index][index], index
        for i in range(index + 1, n):
            if self.Ab[i][index] > best:
                best, ret = self.Ab[i][index], i
        return ret

    def _forward(self):
        n = self._m
        for i in range(n):
            # Ab[i][i] 为主元
            # _max_row，当前行到最后一行
            max_row = self._max_row(i, n)
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]
            # 将主元归一
            self.Ab[i] = self.Ab[i] / self.Ab[i][i]
            for j in range(i + 1, n):
                # 因为i行主元已经归一，让j行减去i行乘以一个常数（self.Ab[j][i]），就达到了消元的目的
                self.Ab[j] = self.Ab[j] - self.Ab[j][i] * self.Ab[i]

    def _backward(self):
        n = self._m
        # 从后向前遍历，直到第0行，步长为1
        for i in range(n - 1, -1, -1):
            # Ab[i][i] 此时是主元
            for j in range(i - 1, -1, -1):
                # j是i上面一行的向量， 只要i行主元乘以一个常数（j行i列），再与j行相减，达到了消元的目的
                self.Ab[j] = self.Ab[j] - self.Ab[j][i] * self.Ab[i]

    # 高斯约旦消元法
    def gauss_jordan_elimination(self):
        # 第一次遍历，找出i行i列最大的值，值越大，矩阵的行越靠前，再找出每一行的主元，进行归一
        self._forward()
        # 第二次从后往前遍历，消灭前面的主元
        self._backward()

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])
