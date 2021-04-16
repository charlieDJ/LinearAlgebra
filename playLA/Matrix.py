from playLA.Vector import Vector


class Matrix:
    def __init__(self, lst2):
        """二维数组赋值为对象成员变量，为了防止浅拷贝，使用列表生成式赋值"""
        self._values = [row[:] for row in lst2]

    @classmethod
    def zero(cls, r, c):
        """创建有r行，c列的零矩阵"""
        return cls([[0] * c for _ in range(r)])

    @classmethod
    def identity(cls, n):
        """返回一个n行n列的单位矩阵"""
        m = [[0] * n for _ in range(n)]
        for i in range(n):
            """从左上到右下，只有i行i列是1，其余全部是0"""
            m[i][i] = 1
        return cls(m)

    def T(self):
        """转置矩阵，行转列，列转行"""
        return Matrix([[e for e in self.col_vector(i)] for i in range(self.col_num())])

    def __add__(self, another):
        """两个矩阵相加"""
        assert self.shape() == another.shape(), \
            "error in adding, shape is not the same!"
        return Matrix([[a + b for a, b in zip(self.row_vector(i), another.row_vector(i))]
                       for i in range(self.row_num())])

    def __sub__(self, another):
        """两个矩阵相减"""
        assert self.shape() == another.shape(), \
            "error in adding, shape is not the same!"
        return Matrix([[a - b for a, b in zip(self.row_vector(i), another.row_vector(i))]
                       for i in range(self.row_num())])

    def __mul__(self, k):
        """矩阵与标量相乘"""
        return Matrix([[e * k for e in self.row_vector(i)] for i in range(self.row_num())])

    def __rmul__(self, k):
        """标量与矩阵相乘"""
        return self * k

    def __truediv__(self, k):
        """矩阵与标量相除"""
        return (1 / k) * self

    def dot(self, another):
        """返回矩阵乘法的结果"""
        if isinstance(another, Vector):
            """矩阵乘以向量"""
            assert self.col_num() == len(another), \
                "Error in Matrix-Vector multiplication"
            return Vector([self.row_vector(i).dot(another) for i in range(self.row_num())])
        if isinstance(another, Matrix):
            """"矩阵乘以矩阵"""
            assert self.col_num() == another.row_num(), \
                "Error in Matrix-Matrix multiplication"
            return Matrix([[self.row_vector(i).dot(another.col_vector(j)) for j in range(another.col_num())]
                           for i in range(self.row_num())])

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def size(self):
        """返回矩阵的元素个数"""
        return self.row_num() * self.col_num()

    def row_vector(self, index):
        """返回矩阵的第index个行向量"""
        return Vector(self._values[index])

    def col_vector(self, index):
        """返回矩阵的第index个列向量"""
        return Vector([row[index] for row in self._values])

    def __getitem__(self, pos):
        """返回第几行，第几列元素"""
        r, c = pos
        return self._values[r][c]

    def shape(self):
        """返回矩阵的形状，行数与列数"""
        return len(self._values), len(self._values[0])

    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__

    def row_num(self):
        return self.shape()[0]

    def col_num(self):
        return self.shape()[1]
