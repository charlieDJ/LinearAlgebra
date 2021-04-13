from playLA.Matrix import Matrix

if __name__ == '__main__':
    matrix = Matrix([[1, 2], [2, 3]])
    print(matrix)
    print("矩阵的形状：{}".format(matrix.shape()))
    print("矩阵的行数：{}，矩阵的列数：{}".format(matrix.row_num(), matrix.col_num()))
    print("矩阵的元素个数：{}".format(matrix.size()))
    print("矩阵元素：{}".format(matrix[1, 1]))
    print("矩阵行向量：{}".format(matrix.row_vector(1)))
    print("矩阵列向量：{}".format(matrix.col_vector(1)))
