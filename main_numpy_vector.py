import numpy as np

if __name__ == "__main__":
    print(np.__version__)
    vec = np.array([1, 2, 3])
    # create vector
    print(np.zeros(5))
    print(np.full(5, 666))
    # array
    splice = vec[0:2]
    print(type(splice))

    vec2 = np.array([4, 5, 6])
    dot = vec2.dot(vec)
    print("vec*vec2={}".format(dot))

    norm = np.linalg.norm(vec)
    print("norm:{}".format(norm))
    # 单位向量
    print( vec / norm)
    # 标准单位向量
    print(np.linalg.norm(vec/norm))