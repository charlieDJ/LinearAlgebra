from playLA.LinearSystem import LinearSystem
from playLA.Matrix import Matrix
from playLA.Vector import Vector

if __name__ == '__main__':
    A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls = LinearSystem(A, b)
    elimination = ls.gauss_jordan_elimination()
    if not elimination:
        print("No solution")
    else:
        print("has solution")
    ls.fancy_print()
