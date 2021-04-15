import math
from ._glabal import EPSILON


class Vector:
    def __init__(self, lst):
        self._values = lst

    def __len__(self):
        return len(self._values)

    @classmethod
    def zero(cls, dim):
        """创建dim维的零向量"""
        return cls([0] * dim)

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(e ** 2 for e in self))

    def normalize(self):
        """归一化"""
        if self.norm() < EPSILON:
            raise ZeroDivisionError('norm can not be zero')
        return Vector(self._values) / self.norm()

    # 向量相加
    def __add__(self, another):
        assert len(self) == len(another), \
            'two Vectors length is not same'
        return Vector([a + b for a, b in zip(self, another)])

    def dot(self, another):
        """点乘的实现方法 x1*x2+y1*y2，对应元素相乘再相加"""
        assert len(self) == len(another), \
            'the vectors length must be the same'
        return sum(a * b for a, b in zip(self, another))

    def __mul__(self, k):
        """返回数量乘法的结果向量 k * self"""
        return Vector([k * x for x in self])

    def __rmul__(self, k):
        return self * k

    def __truediv__(self, k):
        """返回数量除法的结果向量 k / self"""
        return (1 / k) * self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    # 返回向量的迭代器
    def __iter__(self):
        return self._values.__iter__()

    def __getitem__(self, index):
        return self._values[index]

    # 系统调用
    def __repr__(self):
        return "Vector({})".format(self._values)

    # 用户调用
    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
