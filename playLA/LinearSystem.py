from .Matrix import Matrix
from .Vector import Vector
from ._glabal import is_zero


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
        self.pivots = []

    # 查找index行index列最大的值
    def _max_row(self, index_i, index_j, n):
        """ret:最优行数"""
        best, ret = self.Ab[index_i][index_j], index_i
        for i in range(index_i + 1, n):
            if self.Ab[i][index_j] > best:
                best, ret = self.Ab[i][index_j], i
        return ret

    def _forward(self):
        i, k = 0, 0
        while i < self._m and k < self._n:
            # 查看 Ab[i][k] 位置是否可以是主元
            # _max_row，当前行到最后一行
            max_row = self._max_row(i, k, self._m)
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]
            if is_zero(self.Ab[i][k]):
                k += 1
            else:
                # 将主元归一
                self.Ab[i] = self.Ab[i] / self.Ab[i][k]
                for j in range(i + 1, self._m):
                    # 因为i行主元已经归一，让j行减去i行乘以一个常数（self.Ab[j][i]），就达到了消元的目的
                    self.Ab[j] = self.Ab[j] - self.Ab[j][i] * self.Ab[i]
                self.pivots.append(k)
                i += 1

    def _backward(self):
        # 只关心非0行，而0行一般都在增广矩阵最下方
        n = len(self.pivots)
        # 从后向前遍历，直到第0行，步长为1
        for i in range(n - 1, -1, -1):
            k = self.pivots[i]
            # Ab[i][k] 此时是主元
            for j in range(i - 1, -1, -1):
                # j是i上面一行的向量， 只要i行主元乘以一个常数（j行i列），再与j行相减，达到了消元的目的
                self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]

    # 高斯约旦消元法
    def gauss_jordan_elimination(self):
        # 第一次遍历，找出i行i列最大的值，值越大，矩阵的行越靠前，再找出每一行的主元，进行归一
        self._forward()
        # 第二次从后往前遍历，消灭前面的主元
        self._backward()
        """如果有节，返回True，如果没有解，返回False"""
        for i in range(len(self.pivots), self._m):
            if not is_zero(self.Ab[i][-1]):
                return False
        return True

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])
