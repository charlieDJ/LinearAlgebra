import numpy as np

if __name__ == '__main__':
    M1 = np.array([[1, 2], [3, 4]])
    print("M1矩阵：{}".format(M1))
    print("M1矩阵*2:{}".format(M1 * 2))
    vec = np.array([1, 2])
    print("M1矩阵加上向量vec:{}".format(M1 + vec))
    print("M1矩阵转置:{}".format(M1.T))
    print("M1矩阵行向量：{}".format(M1[1]))
    print("M1矩阵列向量：{}".format(M1[:, 1]))
    M2 = np.array([[5, 6], [7, 8]])
    print("M1矩阵乘以M2矩阵：{}".format(M1.dot(M2)))
