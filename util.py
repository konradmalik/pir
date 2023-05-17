import random

def mat_mul(A, B):
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C


def mat_add(A, B):
    return [[(A[i][j] + B[i][j]) for j in range(len(A[0]))]
            for i in range(len(A))]


def mat_sub(A, B):
    return [[(A[i][j] - B[i][j]) for j in range(len(A[0]))]
            for i in range(len(A))]


class Matrix:

    def __init__(self, mod, rows, cols, mat):
        self.mod = mod
        self.rows = rows
        self.cols = cols
        self.mat = [[x % mod for x in row] for row in mat]

    def fill(self, value):
        self.mat = [[value] * self.cols for i in range(self.rows)]

    def __mul__(self, other):
        assert (self.cols == other.rows)
        return Matrix(self.mod, self.rows, other.cols,
                      mat_mul(self.mat, other.mat))

    def __add__(self, other):
        if type(other) == int:
            assert (self.rows == 1 and self.cols == 1)
            return Matrix(self.mod, 1, 1, [[self.mat[0][0] + other]])
        assert (self.rows == other.rows and self.cols == other.cols)
        return Matrix(self.mod, self.rows, self.cols,
                      mat_add(self.mat, other.mat))

    def __sub__(self, other):
        if type(other) == int:
            assert (self.rows == 1 and self.cols == 1)
            return Matrix(self.mod, 1, 1, [[self.mat[0][0] - other]])
        assert (self.rows == other.rows and self.cols == other.cols)
        return Matrix(self.mod, self.rows, self.cols,
                      mat_sub(self.mat, other.mat))

    def __int__(self):
        assert (self.rows == 1 and self.cols == 1)
        return self.mat[0][0]

    def __repr__(self):
        return "Matrix(" + str(self.mat) + ")"


def random_bit():
    return random.randint(0, 1)


def zero_matrix(mod, rows, cols):
    mat = [[0 for _ in range(cols)] for _ in range(rows)]
    return Matrix(mod, rows, cols, mat)


def zero_vector(mod, rows):
    return zero_matrix(mod, rows, 1)


def random_value(mod):
    return random.randint(0, mod - 1)


def random_matrix(mod, rows, cols):
    mat = [[random_value(mod) for _ in range(cols)] for _ in range(rows)]
    return Matrix(mod, rows, cols, mat)


def random_vector(mod, rows):
    return random_matrix(mod, rows, 1)


def random_noise_vector(mod, nd, rows):
    return Matrix(mod, rows, 1,
                  [[random.randint(nd[0], nd[1])] for _ in range(rows)])

