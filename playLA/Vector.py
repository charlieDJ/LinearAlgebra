class Vector:
    def __init__(self, lst):
        self._values = lst

    def __len__(self):
        return len(self._values)

    @classmethod
    def zero(cls, dim):
        """创建dim维的零向量"""
        return cls([0] * dim)

    # 向量相加
    def __add__(self, another):
        assert len(self) == len(another), \
            'two Vectors length is not same'
        return Vector([a + b for a, b in zip(self, another)])

    def __mul__(self, k):
        """向量乘以数量"""
        return Vector([k * x for x in self])

    def __rmul__(self, k):
        return self * k

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
