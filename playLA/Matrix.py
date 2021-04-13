from playLA.Vector import Vector


class Matrix:
    def __init__(self, lst2):
        """二维数组赋值为对象成员变量，为了防止浅拷贝，使用列表生成式赋值"""
        self._values = [row[:] for row in lst2]

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
