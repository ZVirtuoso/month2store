class MatrixHelper:
    @staticmethod
    def transpose(matrix):
        return [list(x) for x in zip(*matrix)]
