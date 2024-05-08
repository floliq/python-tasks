class Matrix:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.data = [[0 for _ in range(self.col)] for _ in range(self.row)]  

    def __str__(self):
        result = ''
        for row in self.data:
            result += ' '.join([str(element) for element in row]) + '\n'
        return result

    def __add__(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError('Невозможно сложить матрицы, размерность матриц разная')
        result = Matrix(self.row, self.col)
        for i in range(self.row):
            for j in range(self.col):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def subtract(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError('Невозможно отнять матрицы, размерность матриц разная')
        result = Matrix(self.row, self.col)
        for i in range(self.row):
            for j in range(self.col):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def multiply(self, other):
        if self.row != other.col:
            raise ValueError('Невозможно отнять матрицы, количество строк одной матрицы не равна количеству столбцой второй')
        result = Matrix(self.row, other.col)
        for i in range(self.row):
            for j in range(other.col):
                for k in range(self.col):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def transpose(self):
        result = Matrix(self.col, self.row)
        for i in range(self.row):
            for j in range(self.col):
                result.data[j][i] = self.data[i][j]
        return result   


m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]
m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]
print("Матрица 1:")
print(m1)
print("Матрица 2:")
print(m2)
print("Сложение матриц:")
print(m1 + m2)
print("Вычитание матриц:")
print(m1.subtract(m2))
m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]
print("Умножение матриц:")
print(m1.multiply(m3))
print("Транспонирование матрицы 1:")
print(m1.transpose())
