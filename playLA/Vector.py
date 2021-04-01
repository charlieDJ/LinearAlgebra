class Vector:
    def __init__(self, lst):
        self._values = lst

    #  系统调用
    def __repr__(self):
        return "Vector({})".format(self._values)

    # 用户调用
    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
