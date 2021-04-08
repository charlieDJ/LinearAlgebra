from playLA.Vector import Vector

if __name__ == '__main__':
    u = Vector([5, 2])
    print(u * 3)
    print(-u)

    # 零向量
    zero2 = Vector.zero(2)
    print(zero2)
