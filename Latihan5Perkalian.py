# Anggelina Kismasari 20051397034 2020MIB

class Matrix :
    def __init__(self, matrix) :
        self.matrix = matrix
    
    def get_row(self, index) :
        try :
            return self.matrix[index][:]
        except :
            return "Index melebihi batasan!"
    
    def get_column(self, index) :
        try :
            column = []
            for row in self.matrix :
                column.append(row[index])
            return column
        except :
            return "Index melebihi batasan!"

    def dot_product(a, b) :
        try :
            return sum([a_i * b_i for a_i, b_i in zip(a, b)])
        except :
            return "Kedua vector harus terhubung!"
    
    def is_multiplicable(a, b) :
        first_matrix, second_matrix = Matrix(a), Matrix(b)
        for i in range(len(a)) :
            row, column = first_matrix.get_row(i), second_matrix.get_column(i)
            if(len(row)) != len(column) :
                return False
        return True
    
    def matrix_multiplication(A, B) :
        if not Matrix.is_multiplicable(A, B) :
            return "Matrix tidak konsisten!"
        row_count, column_count = len(A), len(B[:][0])
        first_matrix, second_matrix = Matrix(A), Matrix(B)
        result_matrix = []
        for i in range(row_count) :
            row_results = []
            for j in range(column_count) :
                row, column = first_matrix.get_row(i), second_matrix.get_column(j)
                row_results.append(Matrix.dot_product(row, column))
            result_matrix.append(row_results)
        return result_matrix

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(A * B)