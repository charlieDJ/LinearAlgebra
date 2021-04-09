from playLA.Vector import Vector

if __name__ == '__main__':
    u = Vector([5, 2])
    print(u * 3)
    print(-u)

    # 零向量
    zero2 = Vector.zero(2)
    print('零向量：{}'.format(zero2))
    norm = u.norm()
    print('u的模为：{}'.format(norm))
    normlize = u.normlize()
    print('u的归一化：{}'.format(normlize))
    try:
        zero2.normlize()
    except ZeroDivisionError:
        print("can not be divided by zero")

    u1 = Vector([3, 1])
    dot = u.dot(u1)
    print('u和u1的点乘结果：{}'.format(dot))
